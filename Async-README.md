# Asynchronous Programming (Async / Await)

This branch demonstrates how to build **asynchronous APIs** in FastAPI using Python's `async` and `await` keywords.



---

## 📌 Concepts Covered

- Asynchronous Programming
- `async` and `await`
- Coroutines
- Non-blocking Operations
- `asyncio`
- FastAPI Async Endpoints

---

## 📖 Overview

This API demonstrates how FastAPI executes asynchronous endpoints using Python's `asyncio` library.

The endpoint simulates a long-running operation by asynchronously waiting for a few seconds before returning a response.

Unlike traditional synchronous functions, asynchronous functions do not block the server while waiting for I/O operations. During this waiting period, FastAPI can continue processing other incoming requests, resulting in better performance under concurrent workloads.

The tutorial also compares synchronous and asynchronous programming patterns to highlight the advantages of non-blocking execution.

---

## 🚀 API Endpoint

### Async Home Endpoint

```
GET /
```

---

## 📤 Example Response

```json
{
    "message": "Async API"
}
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.get()` decorator
- Asynchronous Route Handlers
- `async def`
- `await`
- `asyncio.sleep()`
- Non-blocking Request Processing

---

## ⚖️ Synchronous vs Asynchronous

### Synchronous Execution

- Executes one task at a time.
- Waits for each operation to complete before moving forward.
- Suitable for CPU-bound or simple applications.

### Asynchronous Execution

- Allows multiple tasks to progress concurrently.
- Does not block while waiting for I/O operations.
- Ideal for APIs, databases, file operations, and external service calls.

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Create asynchronous API endpoints.
- Use `async` and `await` in FastAPI.
- Perform non-blocking operations with `asyncio`.
- Differentiate between synchronous and asynchronous execution.
- Build APIs capable of handling concurrent requests efficiently.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.