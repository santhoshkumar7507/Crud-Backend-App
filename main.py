import os
import json
import asyncio

import redis.asyncio as aioredis
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager


# ─────────────────────────────────────────────
#  Redis client (shared across requests)
# ─────────────────────────────────────────────
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
redis_client: aioredis.Redis | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Connect to Redis on startup, disconnect on shutdown."""
    global redis_client
    try:
        redis_client = aioredis.from_url(REDIS_URL, decode_responses=True)
        await redis_client.ping()
        print("✅ Redis connected successfully")
    except Exception as e:
        print(f"⚠️  Redis connection failed: {e} — running without cache")
        redis_client = None
    yield
    if redis_client:
        await redis_client.aclose()
        print("🔌 Redis connection closed")


# ─────────────────────────────────────────────
#  FastAPI App
# ─────────────────────────────────────────────
app = FastAPI(
    title="⚡ CRUD Backend API",
    description=(
        "Production-grade REST API with Redis caching, "
        "built with FastAPI + Uvicorn. Includes simulated DB latency "
        "to demonstrate the power of caching."
    ),
    version="2.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─────────────────────────────────────────────
#  In-memory data store (simulates a database)
# ─────────────────────────────────────────────
items_db: list[dict] = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]


# ─────────────────────────────────────────────
#  Schemas
# ─────────────────────────────────────────────
class ItemCreate(BaseModel):
    name: str | None = None

class ItemResponse(BaseModel):
    id: int
    name: str


# ─────────────────────────────────────────────
#  Helper
# ─────────────────────────────────────────────
async def simulate_db_delay(ms: int = 1000):
    """Simulates a real database query latency."""
    await asyncio.sleep(ms / 1000)


# ─────────────────────────────────────────────
#  Routes
# ─────────────────────────────────────────────

@app.get("/")
async def root():
    return {
        "message": "⚡ CRUD Backend API is running!",
        "version": "2.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.get("/api/items", response_model=list[ItemResponse], summary="Get all items")
async def get_items():
    """
    Fetch all items.

    - **Cache Hit**: Returns instantly from Redis (< 5ms).
    - **Cache Miss**: Simulates a 1-second DB query, then caches the result for 60 seconds.
    """
    # ── Try Redis cache first ──────────────────
    if redis_client:
        try:
            cached = await redis_client.get("items")
            if cached:
                return json.loads(cached)
        except Exception as e:
            print(f"Redis read error: {e}")

    # ── Cache miss → simulate DB latency ──────
    await simulate_db_delay(1000)

    # ── Store result in Redis (TTL = 60s) ─────
    if redis_client:
        try:
            await redis_client.setex("items", 60, json.dumps(items_db))
        except Exception as e:
            print(f"Redis write error: {e}")

    return items_db


@app.get("/api/items/{item_id}", response_model=ItemResponse, summary="Get single item")
async def get_item(item_id: int):
    """Fetch a single item by ID with a simulated 200ms database delay."""
    await simulate_db_delay(200)
    item = next((i for i in items_db if i["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} not found")
    return item


@app.post("/api/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED, summary="Create item")
async def create_item(payload: ItemCreate):
    """Create a new item and append it to the data store."""
    new_item = {
        "id": len(items_db) + 1,
        "name": payload.name or f"New Item {len(items_db) + 1}",
    }
    items_db.append(new_item)

    # Invalidate cache so next GET reflects new data
    if redis_client:
        try:
            await redis_client.delete("items")
        except Exception:
            pass

    return new_item


@app.put("/api/items/{item_id}", response_model=ItemResponse, summary="Update item")
async def update_item(item_id: int, payload: ItemCreate):
    """Update the name of an existing item."""
    item = next((i for i in items_db if i["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} not found")

    item["name"] = payload.name

    # Invalidate cache
    if redis_client:
        try:
            await redis_client.delete("items")
        except Exception:
            pass

    return item


@app.delete("/api/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete item")
async def delete_item(item_id: int):
    """Remove an item from the data store by ID."""
    global items_db
    original_len = len(items_db)
    items_db = [i for i in items_db if i["id"] != item_id]

    if len(items_db) == original_len:
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} not found")

    # Invalidate cache
    if redis_client:
        try:
            await redis_client.delete("items")
        except Exception:
            pass
