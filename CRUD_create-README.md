# Database CRUD – Create Operation

This branch demonstrates how to perform the **Create** operation of CRUD using **FastAPI** and **SQLAlchemy ORM**.

After establishing the database connection and defining ORM models, this tutorial focuses on inserting new records into a SQLite database. It introduces the fundamental workflow of creating database objects, persisting them using SQLAlchemy sessions, and returning the newly created resource.

---

## 📌 Concepts Covered

- Database CRUD (Create)
- SQLAlchemy ORM
- SQLite Database
- Database Sessions
- Dependency Injection
- Data Persistence
- Transaction Management

---

## 📖 Overview

This API demonstrates how to insert a new Todo item into a SQLite database using SQLAlchemy.

The application performs the following operations:

- Establishes a database connection.
- Creates a SQLAlchemy session.
- Constructs a new Todo object.
- Adds the object to the session.
- Commits the transaction.
- Refreshes the object to retrieve generated database values.
- Returns the newly created record as a JSON response.

This tutorial introduces the standard SQLAlchemy workflow used for creating records and serves as the first step toward implementing complete database CRUD operations.

---

## 🚀 API Endpoint

### Create Todo

```
POST /todo
```

### Query Parameter

| Parameter | Type | Description |
|-----------|------|-------------|
| `title` | `string` | Title of the Todo item |

---

## 📤 Example Request

```
POST /todo?title=Learn SQLAlchemy
```

---

## 📥 Example Response

```json
{
    "message": "Todo Created!",
    "data": {
        "id": 1,
        "title": "Learn SQLAlchemy",
        "completed": "False"
    }
}
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.post()` decorator
- Dependency Injection (`Depends`)
- SQLAlchemy ORM
- Database Sessions
- Creating ORM Objects
- `db.add()`
- `db.commit()`
- `db.refresh()`
- JSON Serialization

---

## 🗄 SQLAlchemy Workflow

This tutorial introduces the standard object creation workflow in SQLAlchemy:

1. Create an ORM object.
2. Add it to the current database session.
3. Commit the transaction.
4. Refresh the object.
5. Return the persisted data.

This workflow is commonly used in production FastAPI applications for inserting new records into relational databases.

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Insert new records into a database using SQLAlchemy.
- Work with SQLAlchemy sessions.
- Commit database transactions.
- Retrieve database-generated values after insertion.
- Build the Create operation of a CRUD API.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.