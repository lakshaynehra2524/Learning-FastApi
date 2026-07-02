# Tutorial-01 — Getting Started with FastAPI 🚀

## Overview

This tutorial introduces the basic structure of a FastAPI application. The objective is to understand how to create a FastAPI instance, define API routes, and return simple JSON responses.

This serves as the foundation for all upcoming tutorials in this repository.

## Topics Covered

* Creating a FastAPI application
* Understanding the `FastAPI()` instance
* Defining GET endpoints
* Returning JSON responses
* Running the development server

## Project Structure

```text
.
├── main.py
└── README.md
```

## Endpoints

| Method | Endpoint | Description                    |
| ------ | -------- | ------------------------------ |
| GET    | `/`      | Home endpoint                  |
| GET    | `/about` | About endpoint                 |
| GET    | `/users` | Returns a sample list of users |

## Running the Project

1. Create and activate a virtual environment.
2. Install the required packages:

```bash
pip install fastapi uvicorn
```

3. Start the development server:

```bash
uvicorn main:app --reload
```

4. Open your browser:

* **Application:** http://127.0.0.1:8000
* **Swagger UI:** http://127.0.0.1:8000/docs
* **ReDoc:** http://127.0.0.1:8000/redoc

## Learning Outcome

By the end of this tutorial, you will understand how to:

* Initialize a FastAPI application.
* Create basic API routes.
* Handle simple GET requests.
* Return JSON responses.
* Run and test a FastAPI application locally.

---

➡️ This branch acts as the starting point for the complete FastAPI learning journey. Future tutorial branches will build upon this foundation by introducing routing, path parameters, query parameters, validation, CRUD operations, databases, authentication, and other production-ready FastAPI concepts.
