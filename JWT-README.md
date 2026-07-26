# JWT Authentication

This branch demonstrates how to implement **JSON Web Token (JWT) Authentication** in FastAPI to secure API endpoints.

JWT is one of the most widely used authentication mechanisms in modern REST APIs. After successful authentication, the server generates a signed token that clients include in subsequent requests to access protected resources.

---

## 📌 Concepts Covered

- JSON Web Tokens (JWT)
- User Authentication
- Token Generation
- Token Verification
- Protected Routes
- Dependency Injection
- Authorization
- HTTP Exceptions

---

## 📖 Overview

This API demonstrates the complete authentication flow using JWT in FastAPI.

The application performs the following operations:

- Authenticates user credentials.
- Generates a signed JWT access token.
- Sets an expiration time for the token.
- Verifies incoming JWT tokens.
- Protects API endpoints using dependency injection.
- Returns appropriate error responses for invalid or expired tokens.

This tutorial introduces the fundamental authentication workflow used by many production REST APIs before integrating databases and user management systems.

---

## 🚀 API Endpoints

### User Login

```
POST /login
```

**Query Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `username` | `string` | User's username |
| `password` | `string` | User's password |

---

### Protected Endpoint

```
GET /secure
```

**Header Required**

```
token: <JWT Token>
```

---

## 📥 Example Login Request

```
POST /login?username=admin&password=1234
```

---

## 📤 Example Login Response

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR..."
}
```

---

## 📤 Example Protected Response

```json
{
    "message": "Secure data accessed",
    "user": {
        "sub": "admin",
        "exp": 1750000000
    }
}
```

---

## 📤 Example Error Response

```json
{
    "detail": "Invalid or expired token"
}
```

**Status Code**

```
401 Unauthorized
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.post()` decorator
- `@app.get()` decorator
- Dependency Injection (`Depends`)
- Request Headers
- JWT Token Generation
- JWT Token Verification
- Protected API Routes
- `HTTPException`
- JSON Responses

---

## 🔐 JWT Authentication Workflow

```
Client
   │
   │ Login (Username & Password)
   ▼
FastAPI Server
   │
   │ Validate Credentials
   ▼
Generate JWT Token
   │
   ▼
Return Access Token
   │
   ▼
Client Stores Token
   │
   │
   │ Request Protected Endpoint
   │ Header:
   │ token: <JWT>
   ▼
Verify Token
   │
   ├── Valid  → Return Protected Data ✅
   └── Invalid / Expired → 401 Unauthorized ❌
```

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Generate JWT access tokens.
- Configure token expiration.
- Secure API endpoints using authentication.
- Verify JWT tokens in incoming requests.
- Protect resources using dependency injection.
- Build the foundation for authentication systems in FastAPI.

---

## 🛠 Tech Stack

- Python
- FastAPI
- Python-JOSE
- JWT
- Uvicorn

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.