# Dependency Injection

This branch demonstrates how to use **Dependency Injection** in FastAPI to separate reusable logic from API endpoints.

Dependency Injection is one of FastAPI's core features. It allows common operations such as authentication, authorization, database connections, configuration loading, and validation to be written once and reused across multiple endpoints, resulting in cleaner and more maintainable applications.

---

## 📌 Concepts Covered

- Dependency Injection
- Dependencies with `Depends()`
- Request Header Validation
- Header Parameters
- Authentication Workflow
- HTTP Exceptions
- Reusable Business Logic

---

## 📖 Overview

This API demonstrates how to secure an endpoint using a dependency function.

Before the endpoint is executed, FastAPI automatically calls the dependency to verify an authentication token provided in the request headers.

The dependency performs the following tasks:

- Reads the request header.
- Validates the authentication token.
- Raises an HTTP exception if the token is invalid.
- Returns user information when authentication succeeds.

The endpoint itself remains focused on handling business logic, while authentication is handled independently through dependency injection.

---

## 🚀 API Endpoint

### Access Secure Data

```
GET /secure-data
```

---

## 📥 Required Request Header

```
token: mysecrettoken
```

---

## 📤 Example Success Response

```json
{
    "message": "Secure data accessed",
    "user": {
        "user": "Authorized user"
    }
}
```

---

## 📤 Example Error Response

```json
{
    "detail": "Unauthorized"
}
```

**Status Code**

```
401 Unauthorized
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.get()` decorator
- `Depends()`
- Dependency Injection
- Header Parameters
- `Header()`
- `HTTPException`
- Authentication Flow
- Automatic Dependency Resolution

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Create reusable dependency functions.
- Inject dependencies into API endpoints using `Depends()`.
- Read and validate request headers.
- Implement simple token-based authentication.
- Separate authentication logic from business logic.
- Build cleaner and more maintainable FastAPI applications.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.