# SQLite Database Integration

This branch demonstrates how to connect a **FastAPI** application with an **SQLite** database using Python's built-in `sqlite3` module.

SQLite is a lightweight, file-based relational database that is ideal for learning database concepts, prototyping applications, and developing small to medium-sized projects. This tutorial introduces the fundamentals of database connectivity before moving to ORMs such as SQLAlchemy.

---

## 📌 Concepts Covered

- SQLite Database
- Database Connection
- SQLite3 Module
- SQL Table Creation
- SQL Queries
- Database Initialization
- FastAPI Database Integration

---

## 📖 Overview

This API demonstrates how to establish a connection between FastAPI and an SQLite database.

When the application starts, it performs the following tasks:

- Creates a connection to the SQLite database.
- Initializes a database cursor.
- Creates a **Todos** table if it does not already exist.
- Commits the database changes.
- Exposes an API endpoint confirming successful database connectivity.

This tutorial focuses on database initialization and table creation, laying the groundwork for implementing full database-based CRUD operations in later tutorials.

---

## 🚀 API Endpoint

### Database Status

```
GET /
```

---

## 📤 Example Response

```json
{
    "message": "SQLite connected successfully!"
}
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.get()` decorator
- SQLite Database Connection
- `sqlite3.connect()`
- Database Cursor
- SQL `CREATE TABLE`
- Database Commit Operations

---

## 🗄️ Database Schema

### `todos`

| Column | Type |
|---------|------|
| `id` | INTEGER (Primary Key) |
| `title` | TEXT |
| `completed` | TEXT |

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Connect a FastAPI application to an SQLite database.
- Create a database if it does not already exist.
- Create database tables using SQL statements.
- Execute SQL queries using a cursor.
- Commit database transactions.
- Prepare a FastAPI project for database-driven CRUD operations.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.