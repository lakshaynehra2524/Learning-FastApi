# Database CRUD – Read Operation

This branch demonstrates how to perform the **Read** operation of CRUD using **FastAPI** and **SQLAlchemy ORM**.

Building upon the Create operation, this tutorial focuses on retrieving records from a SQLite database. It covers fetching all records as well as querying a specific record by its unique identifier, while also introducing proper error handling for missing resources.

---

## 📌 Concepts Covered

- Database CRUD (Read)
- SQLAlchemy ORM
- SQLite Database
- Database Sessions
- Querying Records
- Filtering Data
- HTTP Exceptions
- Dependency Injection

---

## 📖 Overview

This API demonstrates how to retrieve Todo items stored in a SQLite database using SQLAlchemy.

The application supports two read operations:

- Retrieve all Todo records.
- Retrieve a specific Todo by its unique ID.

The tutorial introduces SQLAlchemy query methods for reading data from a relational database while integrating FastAPI's dependency injection and exception handling to build reliable REST API endpoints.

---

## 🚀 API Endpoints

### Create Todo

```
POST /todos
```

### Query Parameter

| Parameter | Type | Description |
|-----------|------|-------------|
| `title` | `string` | Title of the Todo item |

---

### Get All Todos

```
GET /todos
```

---

### Get Todo by ID

```
GET /todo/{todo_id}
```

---

## 📤 Example Response (Get All Todos)

```json
{
    "Total": 2,
    "data": [
        {
            "id": 1,
            "title": "Learn FastAPI",
            "completed": "False"
        },
        {
            "id": 2,
            "title": "Learn SQLAlchemy",
            "completed": "False"
        }
    ]
}
```

---

## 📤 Example Response (Get Todo by ID)

```json
{
    "id": 1,
    "title": "Learn FastAPI",
    "completed": "False"
}
```

---

## 📤 Example Error Response

```json
{
    "detail": "Todo not found"
}
```

**Status Code**

```
404 Not Found
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.post()` decorator
- `@app.get()` decorator
- Dependency Injection (`Depends`)
- SQLAlchemy ORM
- Database Sessions
- `db.query()`
- `.all()`
- `.filter()`
- `.first()`
- `HTTPException`
- JSON Serialization

---

## 🗄 SQLAlchemy Query Operations

This tutorial introduces the most common SQLAlchemy read operations:

- Retrieve all records using `.all()`
- Filter records using `.filter()`
- Retrieve the first matching record using `.first()`
- Handle missing records with HTTP exceptions

These query methods form the foundation for reading data in real-world FastAPI applications.

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Retrieve all records from a database.
- Retrieve a specific record using its primary key.
- Filter database queries using SQLAlchemy.
- Handle missing resources with appropriate HTTP exceptions.
- Build RESTful read operations using FastAPI and SQLAlchemy.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.