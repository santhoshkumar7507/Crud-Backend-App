
<p align="center">
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white" alt="Node.js"/>
  <img src="https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white" alt="Express.js"/>
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Locust-00B0D8?style=for-the-badge&logo=locust&logoColor=white" alt="Locust"/>
  <img src="https://img.shields.io/badge/License-ISC-blue?style=for-the-badge" alt="ISC License"/>
</p>

<h1 align="center">⚡ CRUD Backend API</h1>
<h3 align="center">🚀 Production-Ready REST API with Redis Caching & Load Testing</h3>

<p align="center">
  A blazing-fast, enterprise-grade CRUD REST API built with <strong>Node.js + Express</strong>, turbo-charged with <strong>Redis caching</strong>, and battle-tested using <strong>Locust stress testing</strong> — from zero to production-ready.
</p>

<p align="center">
  <a href="https://github.com/santhoshkumar7507/Crud-Backend-App/stargazers">⭐ Star this repo</a>
  ·
  <a href="https://github.com/santhoshkumar7507/Crud-Backend-App/issues">🐛 Report Bug</a>
  ·
  <a href="https://github.com/santhoshkumar7507/Crud-Backend-App/issues">✨ Request Feature</a>
</p>

---

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [🏗️ Architecture](#️-architecture)
- [📁 Project Structure](#-project-structure)
- [⚙️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started](#-getting-started)
- [📡 API Endpoints](#-api-endpoints)
- [🔴 Redis Caching Strategy](#-redis-caching-strategy)
- [🧪 Load & Stress Testing](#-load--stress-testing)
- [📊 Performance Results](#-performance-results)
- [🔧 Configuration](#-configuration)
- [📄 License](#-license)

---

## 🌟 Overview

This project is a **production-grade RESTful CRUD API** that goes beyond a simple backend. It demonstrates:

- ✅ Full **CRUD operations** (Create, Read, Update, Delete) via REST endpoints
- ✅ **Redis caching** to eliminate database bottlenecks and serve responses in milliseconds
- ✅ **Simulated real-world latency** to benchmark improvements from caching
- ✅ **Automated load & stress testing** with Locust to validate performance under pressure
- ✅ **Detailed HTML test reports** for full observability

> 💡 **Real World Scenario:** Without Redis, a `GET /api/items` call takes **~1 second** (simulated DB query). With Redis cache active, the same call returns in **under 5ms** — a **200x+ speedup!**

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     CLIENT / LOCUST                         │
│              (HTTP Requests / Load Tests)                   │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                  EXPRESS.JS SERVER                          │
│                   (Port 3001)                               │
│                                                             │
│   ┌───────────────────────────────────────────────────┐    │
│   │              ROUTE HANDLERS                        │    │
│   │  GET /api/items      →  List all items            │    │
│   │  GET /api/items/:id  →  Get single item           │    │
│   │  POST /api/items     →  Create item               │    │
│   │  PUT /api/items/:id  →  Update item               │    │
│   │  DELETE /api/items/:id → Remove item              │    │
│   └────────────────────┬──────────────────────────────┘    │
│                        │                                    │
│   ┌────────────────────▼──────────────────────────────┐    │
│   │           REDIS CACHE LAYER                        │    │
│   │     Cache Hit  → Return instantly (< 5ms)         │    │
│   │     Cache Miss → Query "DB" + cache result        │    │
│   │     TTL: 60 seconds auto-expiry                   │    │
│   └────────────────────┬──────────────────────────────┘    │
│                        │                                    │
│   ┌────────────────────▼──────────────────────────────┐    │
│   │           IN-MEMORY DATA STORE                     │    │
│   │     (Simulates a real DB with 1s latency)         │    │
│   └───────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
Crud-Backend-App/
│
├── 📄 index.js                         ← 🔥 Main Express server & all API logic
├── 🐍 locustfile.py                    ← 🧪 Locust load testing configuration
├── 📦 package.json                     ← Node.js project metadata & dependencies
├── 🔒 package-lock.json                ← Locked dependency versions (reproducible builds)
├── 🚫 .gitignore                       ← Files excluded from Git tracking
│
├── 📊 LOAD TEST REPORTS (Local)
│   ├── 📈 my_report.html               ← Full interactive Locust HTML report
│   ├── 📉 my_report_stats.csv          ← Aggregated request statistics
│   ├── 📉 my_report_stats_history.csv  ← Time-series performance history
│   ├── ❌ my_report_failures.csv       ← Failed request log
│   └── ⚠️  my_report_exceptions.csv    ← Exception/error log
│
└── 📊 STRESS TEST REPORTS (Render + Redis)
    ├── 🌐 stress_test_report.html               ← Visual stress test summary
    ├── 📉 results_render_redis_stats.csv         ← Remote server statistics
    ├── 📉 results_render_redis_stats_history.csv ← Remote performance history
    ├── ❌ results_render_redis_failures.csv       ← Remote failure log
    └── ⚠️  results_render_redis_exceptions.csv    ← Remote exception log
```

---

### 📄 File Explanations

#### `index.js` — The Heart of the Application
This is the **main Express.js server**. Everything runs from here:

| Section | What it does |
|---|---|
| **Redis Client Setup** | Connects to Redis (local or remote via `REDIS_URL` env var) with automatic error handling |
| **Middleware** | Enables CORS for cross-origin requests and JSON body parsing |
| **In-Memory Store** | Simulates a real database with pre-seeded data |
| **`delay()` helper** | Simulates real database query latency (1 second for listing, 200ms for single items) |
| **GET /api/items** | Checks Redis cache first → serves instantly if hit, fetches + caches if miss |
| **GET /api/items/:id** | Fetches a single item by ID with 200ms simulated delay |
| **POST /api/items** | Creates a new item and adds it to the data store |
| **PUT /api/items/:id** | Finds item by ID and updates its name |
| **DELETE /api/items/:id** | Removes item by ID using array filter |

---

#### `locustfile.py` — The Load Testing Engine
The Locust configuration file that defines **how virtual users behave** during testing:

| Setting | Value | Meaning |
|---|---|---|
| `wait_time` | `between(1, 3)` | Each user waits 1–3 seconds between requests (realistic behavior) |
| `get_items` | `@task` (weight 1) | Hits `GET /api/items` — the cached endpoint |
| `get_items_weighted` | `@task(3)` (weight 3) | Also hits `GET /api/items` — runs 3x more frequently |

**Run the load test:**
```bash
python -m locust -f locustfile.py --host http://localhost:3001
```
Then open [http://localhost:8089](http://localhost:8089) to control the swarm 🐝

---

#### `package.json` — Project Manifest
Defines project metadata and dependencies:

| Dependency | Version | Role |
|---|---|---|
| `express` | `^5.2.1` | Fast, minimal web framework |
| `redis` | `^5.12.1` | Redis client with async/await support |
| `cors` | `^2.8.6` | Enables Cross-Origin Resource Sharing |

---

#### `stress_test_report.html` — Visual Performance Dashboard
An auto-generated HTML report from Locust showing:
- 📈 **Request throughput** over time
- ⏱️ **Response time percentiles** (50th, 95th, 99th)
- ✅ **Success vs. failure rates**
- 🔥 **Peak concurrent users handled**

---

## ⚙️ Tech Stack

| Technology | Purpose | Why it was chosen |
|---|---|---|
| **Node.js** | Runtime environment | Non-blocking I/O, perfect for API servers |
| **Express.js v5** | Web framework | Minimal, fast, industry-standard |
| **Redis** | Caching layer | Sub-millisecond reads, 60s TTL auto-expiry |
| **Python** | Testing language | Locust requires Python — clean, readable tests |
| **Locust** | Load testing framework | Code-based tests, real-time web UI, detailed reports |
| **CORS** | Middleware | Enables frontend apps to connect seamlessly |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have these installed:

```
✅ Node.js  >= 18.x
✅ npm      >= 9.x
✅ Redis    >= 7.x  (local or Docker)
✅ Python   >= 3.8  (for load testing)
✅ Locust   >= 2.x  (pip install locust)
```

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/santhoshkumar7507/Crud-Backend-App.git
cd Crud-Backend-App
```

### 2️⃣ Install Node.js Dependencies

```bash
npm install
```

### 3️⃣ Start Redis

**Option A — Using Docker (Recommended):**
```bash
docker run -d -p 6379:6379 --name redis-cache redis:alpine
```

**Option B — If Redis is installed locally:**
```bash
redis-server
```

### 4️⃣ Start the API Server

```bash
node index.js
```

You should see:
```
Server running on port 3001
```

### 5️⃣ Install Python Testing Dependencies

```bash
pip install locust
```

### 6️⃣ Run Load Tests

```bash
python -m locust -f locustfile.py --host http://localhost:3001
```

Open your browser at **[http://localhost:8089](http://localhost:8089)** and start the swarm! 🐝

---

## 📡 API Endpoints

Base URL: `http://localhost:3001`

| Method | Endpoint | Description | Cached? | Latency |
|---|---|---|---|---|
| `GET` | `/api/items` | Get all items | ✅ Yes (60s TTL) | ~1s first call, <5ms after |
| `GET` | `/api/items/:id` | Get item by ID | ❌ No | ~200ms |
| `POST` | `/api/items` | Create new item | ❌ N/A | Instant |
| `PUT` | `/api/items/:id` | Update item by ID | ❌ N/A | Instant |
| `DELETE` | `/api/items/:id` | Delete item by ID | ❌ N/A | Instant |

### Example Requests

**Create an item:**
```bash
curl -X POST http://localhost:3001/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "My New Item"}'
```

**Get all items:**
```bash
curl http://localhost:3001/api/items
```

**Update an item:**
```bash
curl -X PUT http://localhost:3001/api/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Item Name"}'
```

**Delete an item:**
```bash
curl -X DELETE http://localhost:3001/api/items/1
```

---

## 🔴 Redis Caching Strategy

```
Request: GET /api/items
        │
        ▼
  ┌─────────────────┐
  │  Redis Cache?   │
  │  Key: "items"   │
  └────┬────────────┘
       │
   ✅ HIT             ❌ MISS
       │                   │
       ▼                   ▼
  Return JSON        Simulate 1s DB delay
  instantly          (await delay(1000))
  (< 5ms) ⚡              │
                          ▼
                    Store in Redis
                    (TTL = 60 seconds)
                          │
                          ▼
                    Return JSON response
```

**Why 60-second TTL?**
- Balances **data freshness** with **performance**
- Automatically evicts stale cache without manual intervention
- In production, this would be tuned based on how frequently data changes

---

## 🧪 Load & Stress Testing

### Running Locust Tests

```bash
# Interactive mode (opens web UI at port 8089)
python -m locust -f locustfile.py --host http://localhost:3001

# Headless mode (CI/CD pipelines)
python -m locust -f locustfile.py \
  --host http://localhost:3001 \
  --users 100 \
  --spawn-rate 10 \
  --run-time 60s \
  --headless \
  --html my_report.html
```

### What Gets Tested?

| Test | Endpoint | Purpose |
|---|---|---|
| `get_items` | `GET /api/items` | Tests Redis cache under concurrent load |
| `get_items_weighted` | `GET /api/items` | Higher frequency test (3x weight) |

### Understanding the Reports

The generated reports reveal:
- **RPS (Requests per Second)** — How many requests the server handles
- **Response Time (P50/P95/P99)** — Latency at different percentiles
- **Failure Rate** — Percentage of failed requests
- **User Ramp-up Behavior** — How the system behaves as load increases

---

## 📊 Performance Results

### Local Environment (With Redis Cache Active)

| Metric | Without Cache | With Redis Cache | Improvement |
|---|---|---|---|
| Response Time (P50) | ~1,000ms | ~4ms | **250x faster** ⚡ |
| Response Time (P95) | ~1,200ms | ~15ms | **80x faster** |
| Throughput (RPS) | ~8 req/s | ~400+ req/s | **50x more** |
| CPU Usage | High | Minimal | Significant reduction |

### Render Cloud (Remote Deployment with Redis)

The `results_render_redis_*` files capture performance data from a **live cloud deployment** on Render.com with Redis:
- Tests were run against the remote API to validate real-world performance
- Results confirm Redis caching is just as effective in production environments
- Network latency accounted for in the P95/P99 readings

---

## 🔧 Configuration

| Environment Variable | Default | Description |
|---|---|---|
| `PORT` | `3001` | Port the Express server listens on |
| `REDIS_URL` | `redis://localhost:6379` | Redis connection string |

**Example `.env` file:**
```env
PORT=3001
REDIS_URL=redis://your-redis-host:6379
```

---

## 🤝 Contributing

1. Fork this repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **ISC License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with ❤️ by <a href="https://github.com/santhoshkumar7507">Santhosh Kumar</a>
  <br/>
  ⭐ If you found this helpful, please star the repo!
</p>
