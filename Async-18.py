import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return {
        "message":"Async API"
    }

# Sync structure 
# def task():
#     time.sleep(3)
#     return "Done"

# Async structure
# async def task():
#     await asyncio.sleep(3)
#     return "Done"
