import time
import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get("/sync")
def sync_endpoint():
    time.sleep(3)
    return {"message": "Sync API"}

@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(3)
    return {"message": "Async API"}


# Sync structure 
# def task():
#     time.sleep(3)
#     return "Done"

# Async structure
# async def task():
#     await asyncio.sleep(3)
#     return "Done"
