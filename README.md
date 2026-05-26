
<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Uvicorn-4051B5?style=for-the-badge&logo=gunicorn&logoColor=white" alt="Uvicorn"/>
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis"/>
  <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black" alt="Render"/>
  <img src="https://img.shields.io/badge/Locust-00B0D8?style=for-the-badge&logo=locust&logoColor=white" alt="Locust"/>
  <img src="https://img.shields.io/badge/License-ISC-blue?style=for-the-badge" alt="ISC License"/>
</p>

<h1 align="center">⚡ CRUD Backend API — FastAPI Edition</h1>
<h3 align="center">🐍 Production-Ready REST API · Redis Caching · Auto Docs · Deployed on Render</h3>

<p align="center">
  A blazing-fast, enterprise-grade CRUD REST API rebuilt from the ground up with <strong>FastAPI + Python</strong>,
  supercharged with <strong>async Redis caching</strong>, auto-generated <strong>Swagger/ReDoc docs</strong>,
  battle-tested with <strong>Locust load testing</strong>, and <strong>live-deployed on Render.com</strong>.
</p>

<p align="center">
  <a href="https://github.com/santhoshkumar7507/Crud-Backend-App">📦 Repository</a>
  ·
  <a href="https://github.com/santhoshkumar7507/Crud-Backend-App/issues">🐛 Report Bug</a>
  ·
  <a href="https://github.com/santhoshkumar7507/Crud-Backend-App/issues">✨ Request Feature</a>
</p>

> 🔁 **Migrated from Node.js → FastAPI** for async performance, automatic API docs, and Pythonic simplicity.

---

## 📋 Table of Contents

- [🌟 Why FastAPI?](#-why-fastapi)
- [🏗️ Architecture](#️-architecture)
- [📁 Project Structure](#-project-structure)
- [⚙️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started (Local)](#-getting-started-local)
- [📡 API Endpoints](#-api-endpoints)
- [🔴 Redis Caching Strategy](#-redis-caching-strategy)
- [🧪 Load & Stress Testing](#-load--stress-testing)
- [📊 Performance Results](#-performance-results)
- [☁️ Deployment on Render](#️-deployment-on-render)
- [🔧 Configuration](#-configuration)
- [📄 License](#-license)

---

## 🌟 Why FastAPI?

| Feature | Node.js (Old) | FastAPI (New) ✅ |
|---|---|---|
| Language | JavaScript | Python |
| Performance | Fast | **Equally fast (async/await)** |
| Auto API Docs | ❌ Manual | ✅ **Auto Swagger + ReDoc** |
| Type Safety | Partial | ✅ **Full Pydantic validation** |
| Async Redis | ✅ | ✅ `redis.asyncio` |
| Deployment | Manual | ✅ `render.yaml` auto-config |
| Error Handling | Manual | ✅ **Built-in HTTP exceptions** |

FastAPI is one of the **fastest Python frameworks** available — benchmarked at par with Node.js and Go for I/O-bound tasks, while offering Python's rich ecosystem and developer ergonomics.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                 CLIENT / LOCUST LOAD TESTER                     │
│            (HTTP Requests — GET, POST, PUT, DELETE)             │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│           FASTAPI APPLICATION  (Uvicorn ASGI Server)            │
│                      Port: $PORT (Render) / 8000 (local)        │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │                PYDANTIC VALIDATION LAYER                 │  │
│   │     Auto-validates all request bodies & response types   │  │
│   └───────────────────────────┬─────────────────────────────┘  │
│                               │                                 │
│   ┌───────────────────────────▼─────────────────────────────┐  │
│   │                  ROUTE HANDLERS                          │  │
│   │  GET  /                    →  Health check               │  │
│   │  GET  /api/items           →  List all items             │  │
│   │  GET  /api/items/{id}      →  Get single item            │  │
│   │  POST /api/items           →  Create new item            │  │
│   │  PUT  /api/items/{id}      →  Update item                │  │
│   │  DELETE /api/items/{id}    →  Delete item                │  │
│   │  GET  /docs                →  Swagger UI (auto)          │  │
│   │  GET  /redoc               →  ReDoc UI (auto)            │  │
│   └───────────────────────────┬─────────────────────────────┘  │
│                               │                                 │
│   ┌───────────────────────────▼─────────────────────────────┐  │
│   │              ASYNC REDIS CACHE LAYER                     │  │
│   │   Cache HIT  →  Return instantly  (<5ms) ⚡             │  │
│   │   Cache MISS →  Query data store + cache (TTL 60s)      │  │
│   │   POST/PUT/DELETE → Invalidate cache automatically       │  │
│   └───────────────────────────┬─────────────────────────────┘  │
│                               │                                 │
│   ┌───────────────────────────▼─────────────────────────────┐  │
│   │           IN-MEMORY DATA STORE (simulates DB)            │  │
│   │        [{"id":1,"name":"Item 1"}, ...]                   │  │
│   └─────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    RENDER.COM CLOUD                             │
│           Auto-deploys from GitHub on every push                │
│           Free Redis + Web Service included                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
Crud-Backend-App/
│
├── 🐍 main.py                          ← 🔥 FastAPI app — all routes, Redis, logic
├── 📦 requirements.txt                 ← Python dependencies (fastapi, redis, uvicorn)
├── 🚀 render.yaml                      ← Render.com deployment config (auto-deploy)
├── 🧪 locustfile.py                    ← Locust load testing (4 task types, weighted)
├── 🚫 .gitignore                       ← Ignores venv, pycache, .env, node_modules
│
├── 📊 LOAD TEST REPORTS (Local)
│   ├── 📈 my_report.html               ← Full interactive Locust HTML report
│   ├── 📉 my_report_stats.csv          ← Aggregated request statistics
│   ├── 📉 my_report_stats_history.csv  ← Time-series performance history
│   ├── ❌ my_report_failures.csv       ← Failed request log
│   └── ⚠️  my_report_exceptions.csv    ← Exception/error log
│
└── 📊 STRESS TEST REPORTS (Render + Redis Cloud)
    ├── 🌐 stress_test_report.html               ← Visual cloud stress test summary
    ├── 📉 results_render_redis_stats.csv         ← Remote performance stats
    ├── 📉 results_render_redis_stats_history.csv ← Remote time-series history
    ├── ❌ results_render_redis_failures.csv       ← Remote failure log
    └── ⚠️  results_render_redis_exceptions.csv    ← Remote exception log
```

---

### 📄 File Explanations

---

#### `main.py` — The Heart of the Application 🔥

The **entire FastAPI backend** lives here. Clean, modular, production-ready.

| Section | Code | What it does |
|---|---|---|
| **Lifespan** | `@asynccontextmanager async def lifespan` | Connects Redis on startup, disconnects on shutdown cleanly |
| **CORS Middleware** | `app.add_middleware(CORSMiddleware)` | Allows any frontend to call this API |
| **Pydantic Schemas** | `class ItemCreate(BaseModel)` | Auto-validates all request bodies with type checking |
| **Cache Check** | `redis_client.get("items")` | Checks Redis before hitting the data store |
| **Cache Write** | `redis_client.setex("items", 60, ...)` | Stores result in Redis for 60 seconds |
| **Cache Invalidation** | `redis_client.delete("items")` | Auto-clears cache on write operations (POST/PUT/DELETE) |
| **Simulated Latency** | `asyncio.sleep(1)` | Simulates a real 1-second database query for benchmarking |
| **HTTP Exceptions** | `raise HTTPException(404, ...)` | Returns proper JSON error responses automatically |
| **Auto Docs** | Built-in | `/docs` (Swagger UI) and `/redoc` (ReDoc) auto-generated |

---

#### `requirements.txt` — Python Dependencies 📦

```
fastapi==0.115.5       ← Web framework (async, fast, type-safe)
uvicorn[standard]==0.32.1  ← ASGI server (runs FastAPI)
redis==5.2.1           ← Async Redis client (redis.asyncio)
httpx==0.28.1          ← Async HTTP client (for testing)
pydantic==2.10.4       ← Data validation & serialization
```

Install all with one command:
```bash
pip install -r requirements.txt
```

---

#### `render.yaml` — Cloud Deployment Blueprint ☁️

```yaml
services:
  - type: web
    name: crud-fastapi-backend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: REDIS_URL
        sync: false          ← Set manually in Render dashboard
```

This single file tells Render **exactly** how to:
- Build the Python environment
- Start the Uvicorn ASGI server
- Inject environment variables like `REDIS_URL`

---

#### `locustfile.py` — The Load Testing Engine 🧪

Simulates real-world user behavior with **4 task types** and realistic weights:

| Task | Method | Endpoint | Weight | Why |
|---|---|---|---|---|
| `get_all_items` | GET | `/api/items` | **4x** | Tests Redis cache under heavy concurrent load |
| `get_single_item` | GET | `/api/items/1` | 2x | Tests per-item retrieval with 200ms delay |
| `create_item` | POST | `/api/items` | 1x | Tests write path + cache invalidation |
| `health_check` | GET | `/` | 1x | Tests root endpoint availability |

**Run load tests:**
```bash
python -m locust -f locustfile.py --host http://localhost:8000
# Then open → http://localhost:8089
```

---

## ⚙️ Tech Stack

| Technology | Version | Purpose | Why chosen |
|---|---|---|---|
| **FastAPI** | 0.115.5 | Web framework | Async, auto-docs, type-safe, blazing fast |
| **Python** | 3.11+ | Runtime | Ecosystem, readability, ML-ready |
| **Uvicorn** | 0.32.1 | ASGI server | Production-grade async HTTP server |
| **Redis** | 5.2.1 | Caching | Sub-millisecond reads, async `redis.asyncio` |
| **Pydantic** | 2.10.4 | Validation | Runtime type checking, auto docs schemas |
| **Locust** | 2.x | Load testing | Python-native, real-time web UI, CSV/HTML reports |
| **Render** | — | Cloud hosting | Free tier, auto-deploy from GitHub, managed Redis |

---

## 🚀 Getting Started (Local)

### Prerequisites

```
✅ Python  >= 3.11
✅ pip     >= 23.x
✅ Redis   >= 7.x  (local or Docker)
✅ Locust  (pip install locust)
```

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/santhoshkumar7507/Crud-Backend-App.git
cd Crud-Backend-App
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start Redis

**Option A — Docker (recommended):**
```bash
docker run -d -p 6379:6379 --name redis-cache redis:alpine
```

**Option B — Local Redis:**
```bash
redis-server
```

### 5️⃣ Start the FastAPI Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

You'll see:
```
✅ Redis connected successfully
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### 6️⃣ Explore the Auto-Generated API Docs

| URL | Interface |
|---|---|
| `http://localhost:8000/docs` | 🟢 **Swagger UI** — Interactive API explorer |
| `http://localhost:8000/redoc` | 📘 **ReDoc** — Clean API reference |

### 7️⃣ Run Load Tests

```bash
python -m locust -f locustfile.py --host http://localhost:8000
```

Open **[http://localhost:8089](http://localhost:8089)** → configure users → start the swarm 🐝

---

## 📡 API Endpoints

Base URL: `http://localhost:8000` (local) or your Render URL (cloud)

| Method | Endpoint | Description | Cached? | Latency |
|---|---|---|---|---|
| `GET` | `/` | Health check & API info | ❌ | Instant |
| `GET` | `/api/items` | Get all items | ✅ **Redis (60s TTL)** | ~1s first call, **<5ms** after |
| `GET` | `/api/items/{id}` | Get item by ID | ❌ | ~200ms |
| `POST` | `/api/items` | Create new item | ❌ + cache cleared | Instant |
| `PUT` | `/api/items/{id}` | Update item | ❌ + cache cleared | Instant |
| `DELETE` | `/api/items/{id}` | Delete item | ❌ + cache cleared | Instant |
| `GET` | `/docs` | Swagger UI | ✅ Built-in | Instant |
| `GET` | `/redoc` | ReDoc UI | ✅ Built-in | Instant |

### Example Requests

**Create an item:**
```bash
curl -X POST http://localhost:8000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "My New Item"}'
```

**Get all items (first call ~1s, then <5ms):**
```bash
curl http://localhost:8000/api/items
```

**Update an item:**
```bash
curl -X PUT http://localhost:8000/api/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Name"}'
```

**Delete an item:**
```bash
curl -X DELETE http://localhost:8000/api/items/1
```

---

## 🔴 Redis Caching Strategy

```
  Request: GET /api/items
          │
          ▼
  ┌──────────────────────┐
  │  redis_client.get()  │
  │  Key: "items"        │
  └──────┬───────────────┘
         │
     ✅ HIT                   ❌ MISS
         │                        │
         ▼                        ▼
   Return JSON             asyncio.sleep(1)
   instantly ⚡           (simulate DB delay)
   (< 5ms)                        │
                                  ▼
                          redis_client.setex()
                          Key: "items", TTL: 60s
                                  │
                                  ▼
                           Return JSON response

  On POST / PUT / DELETE:
  ──────────────────────────────────────────
  redis_client.delete("items")  ← Cache invalidated
  → Next GET will re-fetch fresh data
```

**Key Design Decisions:**
- **60-second TTL** — balances freshness vs. speed
- **Write-through invalidation** — cache is cleared on every mutation
- **Graceful fallback** — if Redis is down, API works without cache (just slower)
- **Async operations** — all Redis calls use `redis.asyncio` for non-blocking I/O

---

## 🧪 Load & Stress Testing

### Interactive Mode (with Web UI)

```bash
python -m locust -f locustfile.py --host http://localhost:8000
```

Open [http://localhost:8089](http://localhost:8089), set users and spawn rate, click **Start**!

### Headless Mode (CI/CD & automation)

```bash
python -m locust -f locustfile.py \
  --host http://localhost:8000 \
  --users 100 \
  --spawn-rate 10 \
  --run-time 60s \
  --headless \
  --html my_report.html \
  --csv my_report
```

### Against Live Render Deployment

```bash
python -m locust -f locustfile.py \
  --host https://your-app.onrender.com \
  --users 50 \
  --spawn-rate 5 \
  --run-time 120s \
  --headless \
  --html stress_test_report.html \
  --csv results_render_redis
```

---

## 📊 Performance Results

### Local Benchmark (With Redis Cache Active)

| Metric | Without Cache | With Redis Cache | Improvement |
|---|---|---|---|
| Response Time (P50) | ~1,000ms | **~4ms** | ⚡ **250x faster** |
| Response Time (P95) | ~1,200ms | **~15ms** | ⚡ **80x faster** |
| Throughput (RPS) | ~8 req/s | **~400+ req/s** | 🚀 **50x more** |
| Error Rate | 0% | 0% | ✅ Stable |

### Cloud Benchmark (Render + Redis Cloud)

The `results_render_redis_*` files capture performance from a **live Render.com deployment**:
- Tested against the production API with Redis cloud instance
- Validates that caching is equally effective in distributed cloud environments
- Network latency included in P95/P99 measurements
- Results confirm Redis is a reliable caching solution at scale

---

## ☁️ Deployment on Render

This project includes a `render.yaml` file for **one-click deployment** on [Render.com](https://render.com).

### Step-by-Step Guide

#### 1. Push Code to GitHub
```bash
git add .
git commit -m "FastAPI CRUD backend with Redis"
git push origin main
```

#### 2. Create a Redis Instance on Render
1. Go to [render.com/dashboard](https://render.com/dashboard)
2. Click **+ New** → **Redis**
3. Name it `crud-redis`, select **Free** plan
4. Click **Create Redis**
5. Copy the **Internal Redis URL** (looks like `redis://red-xxxx:6379`)

#### 3. Deploy the Web Service
1. Click **+ New** → **Web Service**
2. Connect your **GitHub repository**
3. Render auto-detects `render.yaml` settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Add environment variable:
   - **Key:** `REDIS_URL`
   - **Value:** Paste the Internal Redis URL from Step 2
5. Click **Create Web Service**

#### 4. Your API is Live! 🎉
```
https://crud-fastapi-backend.onrender.com/
https://crud-fastapi-backend.onrender.com/docs     ← Swagger UI
https://crud-fastapi-backend.onrender.com/api/items
```

> ⚠️ **Free Tier Note:** Render free services spin down after 15 minutes of inactivity. The first request may take ~30s to cold-start.

---

## 🔧 Configuration

| Environment Variable | Default | Description |
|---|---|---|
| `PORT` | `8000` (local) / auto (Render) | Port for Uvicorn server |
| `REDIS_URL` | `redis://localhost:6379` | Redis connection string |

**Local `.env` file** (never commit this!):
```env
REDIS_URL=redis://localhost:6379
PORT=8000
```

---

## 🤝 Contributing

1. Fork this repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'feat: add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **ISC License**.

---

<p align="center">
  Built with ❤️ and ☕ by <a href="https://github.com/santhoshkumar7507">Santhosh Kumar</a>
  <br/>
  🐍 Powered by FastAPI · ⚡ Cached by Redis · ☁️ Deployed on Render
  <br/><br/>
  ⭐ If this project helped you, please star the repo!
</p>
