# FastAPI Async + Load Challenge

## Setup

```bash
pip install -r requirements.txt
```

## Task

This FastAPI service works fine with a single request but degrades badly
under concurrent load.

1. Run the app:
   ```bash
   uvicorn main:app --reload
   ```

2. Run the load test:
   ```bash
   locust -f locustfile.py --host http://localhost:8000
   ```
   Open http://localhost:8089, simulate 50 users, spawn rate 10, and watch
   the response time chart.

3. Use AI to find why latency spikes under concurrency and fix it.

4. Also check: is the Docker/uvicorn deployment setup itself a bottleneck?

5. Be ready to explain your fix — not just paste it. You'll be asked to
   walk through *why* the original code behaves this way under load.

6. If this were backed by a real database, what would you check about the
DB's own connection pool limits before touching the app code?
