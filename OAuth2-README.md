# OAuth2 Authentication with JWT

This branch demonstrates how to implement **OAuth2 Password Flow** with **JWT Authentication** in FastAPI.

OAuth2 is the industry-standard authorization framework used by modern web applications and APIs. Combined with JWT and secure password hashing, it provides a scalable and secure authentication mechanism for protecting API endpoints.

---

## 📌 Concepts Covered

- OAuth2 Password Flow
- JWT Authentication
- Password Hashing
- Password Verification
- Bearer Token Authentication
- Protected Routes
- Dependency Injection
- Token Validation

---

## 📖 Overview

This API demonstrates a complete authentication workflow using OAuth2 and JWT in FastAPI.

The application performs the following operations:

- Accepts user credentials through an OAuth2 login form.
- Securely verifies passwords using bcrypt hashing.
- Generates a JWT access token upon successful authentication.
- Validates incoming bearer tokens.
- Protects API endpoints using dependency injection.
- Returns appropriate authentication errors for invalid credentials or expired tokens.

Unlike the previous JWT tutorial, this implementation follows the standard OAuth2 Password Bearer workflow used by production-grade REST APIs.

---

## 🚀 API Endpoints

### User Login

```
POST /login
```

**Form Data**

| Parameter | Type | Description |
|-----------|------|-------------|
| `username` | `string` | User's username |
| `password` | `string` | User's password |

---

### Protected Endpoint

```
GET /protected
```

**Authorization Header**

```
Authorization: Bearer <JWT Token>
```

---

## 📥 Example Login Request

```
POST /login
```

**Form Data**

```text
username=admin
password=1234
```

---

## 📤 Example Login Response

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}
```

---

## 📤 Example Protected Response

```json
{
    "message": "Hello you have access to this protected route!",
    "user": "admin"
}
```

---

## 📤 Example Error Response

```json
{
    "detail": "Invalid token"
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
- `OAuth2PasswordBearer`
- `OAuth2PasswordRequestForm`
- Dependency Injection (`Depends`)
- Password Hashing with bcrypt
- Password Verification
- JWT Token Generation
- JWT Token Validation
- Protected API Routes
- `HTTPException`

---

## 🔐 OAuth2 Authentication Workflow

```
Client
   │
   │ Submit Login Form
   ▼
FastAPI Server
   │
   │ Verify Username
   │
   ▼
Verify Password (bcrypt)
   │
   ▼
Generate JWT Access Token
   │
   ▼
Return Bearer Token
   │
   ▼
Client Stores Token
   │
   │
   │ Authorization: Bearer <JWT>
   ▼
Protected Endpoint
   │
   ▼
Validate JWT Token
   │
   ├── Valid Token → Access Granted ✅
   └── Invalid / Expired Token → 401 Unauthorized ❌
```

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Implement OAuth2 Password Flow in FastAPI.
- Hash and verify passwords securely using bcrypt.
- Generate JWT access tokens after authentication.
- Authenticate users using Bearer tokens.
- Protect API endpoints with dependency injection.
- Build authentication systems following modern REST API standards.

---

## 🛠 Tech Stack

- Python
- FastAPI
- Python-JOSE
- OAuth2
- JWT
- Passlib (bcrypt)
- Uvicorn

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.