# POST API

This branch demonstrates how to create a **POST endpoint** in FastAPI to receive data from a client and process it using **Pydantic Models**.

Unlike GET requests, POST requests allow clients to send structured data in the request body, making them ideal for creating new resources in REST APIs.

---

## 📌 Concepts Covered

- POST Requests
- Request Body
- Pydantic Models
- Data Validation
- Automatic JSON Parsing
- JSON Response

---

## 📖 Overview

This API accepts user information through a POST request.

When a request is received, FastAPI:

- Reads the JSON request body.
- Validates the incoming data using a Pydantic model.
- Automatically converts the JSON into a Python object.
- Returns a confirmation message along with the validated data.

If any required field is missing or has an incorrect data type, FastAPI automatically returns a validation error without additional validation logic.

---

## 🚀 API Endpoint

```
POST /Createuser
```

### Example Request Body

```json
{
    "name": "Lakshay",
    "age": 22
}
```

### Example Response

```json
{
    "message": "User created!",
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
- Pydantic `BaseModel`
- Request Body Handling
- Automatic Data Validation
- Automatic JSON Serialization

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Create POST endpoints.
- Receive data through the request body.
- Define request schemas using Pydantic.
- Validate incoming data automatically.
- Return structured JSON responses.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a single concept, creating a structured, chapter-wise learning journey from FastAPI fundamentals to advanced API development.
