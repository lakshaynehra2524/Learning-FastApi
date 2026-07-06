# Exception Handling

This branch demonstrates how to implement **Custom Exception Handling** in FastAPI by creating user-defined exceptions and registering global exception handlers.

Proper exception handling is an essential part of API development. Instead of returning generic error messages, FastAPI allows developers to create custom exceptions that provide meaningful, consistent, and structured error responses.

---

## 📌 Concepts Covered

- Custom Exceptions
- Exception Handlers
- Global Error Handling
- HTTP Error Responses
- JSON Responses
- API Error Management

---

## 📖 Overview

This API demonstrates how to handle application-specific errors using custom exception classes and FastAPI's built-in exception handling system.

The application includes:

- Creating a custom exception.
- Registering a global exception handler.
- Returning structured JSON error responses.
- Sending appropriate HTTP status codes for application-specific errors.

Instead of relying solely on `HTTPException`, this approach enables centralized error handling, making APIs easier to maintain, extend, and standardize across larger applications.

---

## 🚀 API Endpoint

### Get User

```
GET /user/{name}
```

---

## 📤 Example Success Response

```json
{
    "name": "lakshay"
}
```

---

## 📤 Example Error Response

```json
{
    "status": "error",
    "message": "User Rahul not found"
}
```

**Status Code**

```
404 Not Found
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.get()` decorator
- Custom Exception Classes
- `@app.exception_handler()`
- Request Object
- `JSONResponse`
- Global Exception Handling
- Structured Error Responses

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Create custom exception classes.
- Register global exception handlers.
- Return structured JSON error responses.
- Improve API consistency through centralized error handling.
- Build scalable APIs with reusable exception management.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.