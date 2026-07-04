# CRUD Operations

This branch demonstrates how to build a simple **CRUD (Create, Read, Update)** API using FastAPI.

CRUD operations form the foundation of most RESTful APIs. In this tutorial, a simple in-memory list is used to simulate database operations, allowing the focus to remain on understanding API endpoints and request handling before introducing database integration.

---

## 📌 Concepts Covered

- CRUD Operations
- GET Requests
- POST Requests
- PUT Requests
- Path Parameters
- Request Body Validation
- Pydantic Models
- JSON Responses
- In-Memory Data Storage

---

## 📖 Overview

This API manages a collection of **Todo** items.

Each Todo contains:

- ID
- Title
- Completion Status

The application supports the following operations:

- Create a new Todo.
- Retrieve all Todos.
- Retrieve a specific Todo by its ID.
- Update an existing Todo.

Instead of using a database, Todo objects are temporarily stored in a Python list, making it easier to understand the workflow of CRUD operations before introducing persistent storage.

FastAPI automatically validates incoming request data using Pydantic models and serializes Python objects into JSON responses.

---

## 🚀 API Endpoints

### Create Todo

```
POST /todos
```

### Get All Todos

```
GET /todos
```

### Get Todo by ID

```
GET /todos/{todo_id}
```

### Update Todo

```
PUT /todos/{todo_id}
```

---

## 📥 Example Request

```json
{
    "id": 1,
    "title": "Learn FastAPI",
    "completed": false
}
```

---

## 📤 Example Response

```json
{
    "message": "Todo added!",
    "data": {
        "id": 1,
        "title": "Learn FastAPI",
        "completed": false
    }
}
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.get()` decorator
- `@app.post()` decorator
- `@app.put()` decorator
- Path Parameters
- Request Body Handling
- Pydantic Models
- Automatic Data Validation
- JSON Serialization
- Basic CRUD API Design

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Design RESTful CRUD endpoints.
- Create new resources using POST requests.
- Retrieve single and multiple resources using GET requests.
- Update existing resources using PUT requests.
- Validate request bodies with Pydantic.
- Work with path parameters.
- Build a complete CRUD workflow before integrating a database.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.