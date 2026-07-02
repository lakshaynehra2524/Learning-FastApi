# Dynamic Routes

This branch demonstrates how to create **dynamic URL routes** in FastAPI using **Path Parameters**.

Instead of defining a fixed URL, FastAPI allows values to be passed directly through the URL path and automatically validates them according to the specified data type.

---

## 📌 Concepts Covered

- Dynamic URL routing
- Path Parameters
- Type Hinting
- Automatic Data Validation
- JSON Responses

---

## 📖 Overview

The API exposes a route that accepts a **User ID** directly from the URL.

When a request is made, FastAPI:

- Extracts the value from the URL.
- Converts it to the specified Python data type.
- Validates the input automatically.
- Returns the value as a JSON response.

If an invalid data type is provided, FastAPI automatically returns an appropriate validation error without requiring additional code.

---

## 🚀 Example Route

```
GET /users/{user_id}
```

Example:

```
GET /users/25
```

Response:

```json
{
    "user_id": 25
}
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.get()` decorator
- Path Parameters
- Integer type validation
- Automatic JSON serialization

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Create dynamic API endpoints.
- Capture values directly from URL paths.
- Use Python type hints for validation.
- Build cleaner and more flexible REST APIs.

---

## 🛠 Tech Stack

- Python
- FastAPI
- Uvicorn

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where every branch represents a separate tutorial. Each branch focuses on one concept to maintain a structured, chapter-wise learning journey.
