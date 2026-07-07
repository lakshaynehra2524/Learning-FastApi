# Middleware

This branch demonstrates how to implement **Middleware** in FastAPI to intercept HTTP requests and responses.

Middleware acts as a processing layer between the client and the API endpoint. It allows developers to execute logic before a request reaches an endpoint and after the endpoint generates a response. This makes middleware ideal for tasks such as logging, authentication, request timing, monitoring, and performance analysis.

---

## 📌 Concepts Covered

- Middleware
- Request Lifecycle
- Response Lifecycle
- Request Logging
- Performance Measurement
- Request & Response Processing
- FastAPI Middleware

---

## 📖 Overview

This API demonstrates how middleware can intercept every incoming HTTP request and outgoing response.

The middleware performs the following operations:

- Receives every incoming request.
- Records the request start time.
- Passes the request to the appropriate endpoint.
- Calculates the total processing time.
- Logs the requested path and execution time.
- Returns the original response to the client.

Unlike endpoint-specific logic, middleware automatically executes for every request, making it useful for implementing application-wide functionality.

---

## 🚀 Middleware Flow

```text
Client Request
      │
      ▼
Middleware (Before Request)
      │
      ▼
API Endpoint
      │
      ▼
Middleware (After Response)
      │
      ▼
Client Response
```

---

## 📤 Example Console Output

```text
Path: /docs | Time: 0.0018
Path: /secure-data | Time: 0.0032
Path: /openapi.json | Time: 0.0021
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.middleware()` decorator
- Request Object
- `call_next()`
- Request Processing
- Response Processing
- Execution Time Measurement
- Request Logging

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Create custom middleware in FastAPI.
- Intercept incoming requests and outgoing responses.
- Measure request execution time.
- Log request information.
- Implement application-wide functionality without modifying individual endpoints.
- Understand the request-response lifecycle in FastAPI.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.