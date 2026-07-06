# Status Codes & HTTP Exceptions

This branch demonstrates how to use **HTTP Status Codes** and **HTTP Exceptions** in FastAPI to provide meaningful responses for different API outcomes.

Status codes are a fundamental part of REST APIs. They communicate whether a request was successful or why it failed, enabling clients to handle responses appropriately.

---

## 📌 Concepts Covered

- HTTP Status Codes
- Custom Status Codes
- HTTP Exceptions
- Error Handling
- Response Messages
- REST API Best Practices

---

## 📖 Overview

This API demonstrates how FastAPI handles both successful and unsuccessful requests using appropriate HTTP status codes.

The application includes:

- Creating a resource with a custom success status code.
- Returning successful API responses.
- Raising HTTP exceptions for invalid requests.
- Sending meaningful error messages to API clients.

FastAPI provides built-in support for standard HTTP status codes and exception handling, allowing APIs to produce consistent and informative responses with minimal code.

---

## 🚀 API Endpoints

### Create User

```
POST /create_user
```

**Success Status Code**

```
201 Created
```

---

### Get User Details

```
GET /user
```

**Success Status Code**

```
200 OK
```

---

### Get User by ID

```
GET /user/{user_id}
```

**Possible Responses**

- `200 OK`
- `404 Not Found`

---

## 📤 Example Success Response

```json
{
    "status": "success",
    "message": "User fetched",
    "user": {
        "name": "Lakshay",
        "age": 22
    }
}
```

---

## 📤 Example Error Response

```json
{
    "detail": "User Not Found"
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
- `@app.post()` decorator
- `status` module
- `HTTPException`
- Custom HTTP Status Codes
- Exception Handling
- JSON Responses

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Return appropriate HTTP status codes.
- Customize response status codes.
- Raise HTTP exceptions for invalid requests.
- Build APIs that follow RESTful response standards.
- Improve client-side error handling through meaningful API responses.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.