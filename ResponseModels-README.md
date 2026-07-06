# Response Models

This branch demonstrates how to use **Response Models** in FastAPI to control the data returned by an API endpoint.

Response models allow developers to define the exact structure of the response sent to clients. They help prevent sensitive information from being exposed while ensuring consistent and well-documented API responses.

---

## 📌 Concepts Covered

- Response Models
- Data Filtering
- Pydantic Models
- Automatic Response Validation
- JSON Serialization
- API Response Security

---

## 📖 Overview

This API returns information about a user while demonstrating how FastAPI filters response data using a dedicated response model.

The application defines two Pydantic models:

- A complete user model containing all user information.
- A response model containing only the fields intended for API clients.

Although the endpoint returns additional data internally, FastAPI automatically filters the response according to the specified response model before sending it to the client.

This approach helps protect sensitive information such as passwords, tokens, or confidential fields without requiring manual filtering.

---

## 🚀 API Endpoint

### Get User

```
GET /user
```

---

## 📤 Example Response

```json
{
    "name": "Lakshay",
    "age": 22
}
```

> **Note:** Although the endpoint internally includes a `password` field, it is automatically excluded from the response because it is not defined in the response model.

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.get()` decorator
- Pydantic Models
- `response_model`
- Automatic Response Validation
- Automatic Data Filtering
- JSON Serialization

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Create response models using Pydantic.
- Control the structure of API responses.
- Hide sensitive information from clients.
- Improve API consistency and security.
- Build cleaner and more maintainable REST APIs.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.