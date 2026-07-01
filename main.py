import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

# Simulates a DB connection pool limit
db_semaphore = asyncio.Semaphore(1)


async def query_db(item_id: int):
    async with db_semaphore:
        time.sleep(0.2)  # simulates blocking DB driver call
        return {"item_id": item_id, "data": "result"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    result = await query_db(item_id)
    return result


@app.get("/health")
async def health():
    return {"status": "ok"}
