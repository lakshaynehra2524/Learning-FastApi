# Database CRUD – Update Operation

This branch demonstrates how to perform the **Update** operation of CRUD using **FastAPI** and **SQLAlchemy ORM**.

Building upon the Create and Read operations, this tutorial focuses on modifying existing records stored in a SQLite database. It introduces the standard SQLAlchemy workflow for locating a record, updating its fields, committing the transaction, and returning the updated resource.

---

## 📌 Concepts Covered

- Database CRUD (Update)
- SQLAlchemy ORM
- SQLite Database
- Database Sessions
- Updating Records
- Query Filtering
- HTTP Exceptions
- Dependency Injection

---

## 📖 Overview

This API demonstrates how to update Todo items stored in a SQLite database using SQLAlchemy.

The application supports the following operations:

- Create a new Todo.
- Retrieve all Todo records.
- Retrieve a Todo by its ID.
- Update the title of an existing Todo.

When an update request is received, the application first searches for the requested record. If the Todo exists, its data is modified, the transaction is committed, and the updated record is returned. If no matching Todo is found, the API returns an appropriate HTTP error response.

---

## 🚀 API Endpoints

### Create Todo

```
POST /todos
```

**Query Parameter**

| Parameter | Type | Description |
|-----------|------|-------------|
| `title` | `string` | Title of the Todo |

---

### Get All Todos

```
GET /todos
```

---

### Get Todo by ID

```
GET /todos/{todo_id}
```

---

### Update Todo

```
PUT /todos/{todo_id}
```

**Query Parameter**

| Parameter | Type | Description |
|-----------|------|-------------|
| `title` | `string` | Updated title for the Todo |

---

## 📥 Example Update Request

```
PUT /todos/1?title=Master%20FastAPI
```

---

## 📤 Example Success Response

```json
{
    "message": "Todo updated successfully",
    "data": {
        "id": 1,
        "title": "Master FastAPI",
        "completed": true
    }
}
```

---

## 📤 Example Error Response

```json
{
    "detail": "Todo not found!"
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
- `@app.put()` decorator
- Dependency Injection (`Depends`)
- SQLAlchemy ORM
- Database Sessions
- Query Filtering
- Updating ORM Objects
- `db.commit()`
- `db.refresh()`
- `HTTPException`
- JSON Serialization

---

## 🗄 SQLAlchemy Update Workflow

This tutorial introduces the standard SQLAlchemy update process:

1. Retrieve the target record.
2. Verify that the record exists.
3. Modify the required fields.
4. Commit the transaction.
5. Refresh the ORM object.
6. Return the updated record.

This workflow is commonly used when implementing update operations in production FastAPI applications.

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Update existing database records.
- Retrieve records before modification.
- Commit updates using SQLAlchemy.
- Refresh ORM objects after database transactions.
- Handle update failures with HTTP exceptions.
- Build RESTful update endpoints using FastAPI.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.