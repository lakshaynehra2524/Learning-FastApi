# Path Parameters, Query Parameters & Request Body

This branch demonstrates how to combine **Path Parameters**, **Query Parameters**, and **Request Body** in a single FastAPI endpoint.

Many real-world APIs require data from multiple sources within a single request. FastAPI makes it easy to handle route parameters, optional query parameters, and structured request bodies together while providing automatic validation and type conversion.

---

## 📌 Concepts Covered

- Path Parameters
- Query Parameters
- Request Body
- Pydantic Models
- PUT Requests
- Automatic Data Validation
- JSON Serialization

---

## 📖 Overview

This API manages a simple collection of users stored in memory.

It demonstrates two common API operations:

- Creating a new user using a POST request.
- Updating an existing user using a PUT request.

The update endpoint combines three different types of inputs:

- **Path Parameter** to identify the user.
- **Request Body** to receive updated user information.
- **Query Parameter** to control optional behavior during the request.

FastAPI automatically validates each input source and converts incoming data into appropriate Python objects before passing it to the endpoint function.

---

## 🚀 API Endpoints

### Create User

```
POST /users
```

### Update User

```
PUT /users/{user_id}?notify=true
```

---

## 📥 Example Request Body

```json
{
    "name": "Lakshay",
    "age": 22
}
```

---

## 📤 Example Response

```json
{
    "message": "User Updated",
    "notify": true,
    "data": {
        "name": "Lakshay",
        "age": 22
    }
}
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.post()` decorator
- `@app.put()` decorator
- Path Parameters
- Query Parameters
- Request Body Handling
- Pydantic Models
- Automatic Type Validation
- Automatic JSON Serialization

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Combine path parameters, query parameters, and request bodies within a single endpoint.
- Build update operations using PUT requests.
- Validate structured request data with Pydantic.
- Handle multiple input sources in FastAPI.
- Design cleaner and more flexible REST API endpoints.

---

## 🛠 Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.