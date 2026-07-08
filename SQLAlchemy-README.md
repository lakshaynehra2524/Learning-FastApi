# SQLAlchemy ORM Integration

This branch demonstrates how to integrate **SQLAlchemy ORM** with FastAPI to establish a database connection and define database models.

SQLAlchemy is one of the most widely used Object Relational Mapping (ORM) libraries in Python. It enables developers to interact with relational databases using Python classes instead of writing raw SQL queries.

---

## 📌 Concepts Covered

- SQLAlchemy ORM
- SQLite Database
- Database Engine
- Session Management
- Declarative Models
- Dependency Injection
- Database Table Creation

---

## 📖 Overview

This API demonstrates the initial setup required to integrate SQLAlchemy with a FastAPI application.

The application includes:

- Configuring a SQLite database.
- Creating a SQLAlchemy engine.
- Establishing database sessions.
- Defining ORM models using declarative classes.
- Automatically creating database tables.
- Managing database connections using FastAPI dependencies.

Although this tutorial focuses on database configuration and connectivity, it lays the foundation for implementing full database CRUD operations in upcoming tutorials.

---

## 🚀 API Endpoint

### Database Connection Test

```
GET /
```

---

## 📤 Example Response

```json
{
    "message": "DB connected!"
}
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- Dependency Injection (`Depends`)
- SQLAlchemy Engine
- Session Management
- Declarative Base
- ORM Models
- Database Table Creation
- SQLite Integration

---

## 🗄 Database Components

This tutorial introduces the core building blocks of SQLAlchemy:

- Database Engine
- Session Factory
- Declarative Base
- ORM Model Definition
- Database Dependency
- Automatic Table Creation

These components form the foundation for performing database CRUD operations in later tutorials.

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Connect a FastAPI application to a SQLite database.
- Configure a SQLAlchemy engine.
- Create database sessions.
- Define ORM models using Python classes.
- Automatically generate database tables.
- Manage database connections using dependency injection.

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.