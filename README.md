# Pydantic Models (Nested Models)

This branch demonstrates how to use **Nested Pydantic Models** in FastAPI to represent structured and hierarchical data.

Real-world APIs often deal with complex objects rather than simple flat data. Pydantic allows one model to contain another model, making request validation more organized, scalable, and easier to maintain.

---

## 📌 Concepts Covered

- Pydantic Models
- Nested Models
- Request Body Validation
- Data Modeling
- JSON Serialization
- Automatic Type Validation

---

## 📖 Overview

This API accepts user information where the request contains both personal details and a nested address object.

When a request is received, FastAPI:

- Reads the JSON request body.
- Validates the complete request structure.
- Validates nested objects automatically.
- Converts the JSON into nested Python objects.
- Returns the validated data as a JSON response.

If any required field is missing or contains an invalid data type, FastAPI automatically returns a detailed validation error without requiring manual validation logic.

---

## 🚀 API Endpoint

```
POST /Createuser
```

### Example Request Body

```json
{
    "name": "Lakshay",
    "age": 22,
    "address": {
        "city": "Rohtak",
        "pincode": "124001"
    }
}
```

### Example Response

```json
{
    "name": "Lakshay",
    "age": 22,
    "address": {
        "city": "Rohtak",
        "pincode": "124001"
    }
}
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.post()` decorator
- Pydantic `BaseModel`
- Nested Pydantic Models
- Request Body Handling
- Automatic Data Validation
- Automatic JSON Serialization

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Create multiple Pydantic models.
- Build nested request schemas.
- Validate hierarchical JSON data.
- Design structured API request bodies.
- Develop APIs capable of handling real-world complex data models.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a single FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to advanced API development.
