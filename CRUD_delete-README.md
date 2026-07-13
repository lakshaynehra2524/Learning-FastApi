# Database CRUD – Delete Operation

This branch demonstrates how to perform the **Delete** operation of CRUD using **FastAPI** and **SQLAlchemy ORM**.

Completing the CRUD series, this tutorial focuses on permanently removing records from a SQLite database. It introduces the standard SQLAlchemy workflow for locating a record, validating its existence, deleting it from the database, and committing the transaction.

---

## 📌 Concepts Covered

- Database CRUD (Delete)
- SQLAlchemy ORM
- SQLite Database
- Database Sessions
- Record Deletion
- Query Filtering
- HTTP Exceptions
- Dependency Injection

---

## 📖 Overview

This API demonstrates how to delete Todo items stored in a SQLite database using SQLAlchemy.

The application now supports the complete CRUD workflow:

- Create a new Todo.
- Retrieve all Todo records.
- Retrieve a Todo by its ID.
- Update an existing Todo.
- Delete a Todo from the database.

Before deleting a record, the application verifies that the requested Todo exists. If found, it removes the record from the database and commits the transaction. Otherwise, an appropriate HTTP error response is returned.

This tutorial completes the implementation of a fully functional CRUD API using FastAPI and SQLAlchemy.

---

## 🚀 API Endpoints

### Create Todo

```
POST /todos
```

**Query Parameter**

| Parameter | Type | Description |
|----------|------|-------------|
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
|----------|------|-------------|
| `title` | `string` | Updated title for the Todo |

---

### Delete Todo

```
DELETE /todos/{todo_id}
```

---

## 📤 Example Success Response

```json
{
    "message": "TODO Deleted"
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
- `@app.put()` decorator
- `@app.delete()` decorator
- Dependency Injection (`Depends`)
- SQLAlchemy ORM
- Database Sessions
- Query Filtering
- Record Deletion
- `db.delete()`
- `db.commit()`
- `HTTPException`
- JSON Serialization

---

## 🗄 SQLAlchemy Delete Workflow

This tutorial introduces the standard SQLAlchemy delete process:

1. Retrieve the target record.
2. Verify that the record exists.
3. Delete the ORM object.
4. Commit the transaction.
5. Return a confirmation response.

This workflow is commonly used when implementing delete operations in production FastAPI applications.

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Delete records from a relational database.
- Locate resources before deletion.
- Remove ORM objects using SQLAlchemy.
- Commit delete transactions.
- Handle deletion failures with HTTP exceptions.
- Build the complete CRUD lifecycle using FastAPI and SQLAlchemy.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.