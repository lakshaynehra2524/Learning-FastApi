# API Testing with Pytest

This branch demonstrates how to perform **automated API testing** in FastAPI using **Pytest** and FastAPI's `TestClient`.

Testing is an important part of API development because it helps verify that endpoints return the expected status codes and response data after changes are made to the application.

---

## 📌 Concepts Covered

- Pytest
- FastAPI TestClient
- Automated API Testing
- Test Functions
- HTTP Status Code Assertions
- JSON Response Assertions
- Query Parameters Testing

---

## 📖 Overview

This branch demonstrates how to create and execute basic automated tests for a FastAPI application.

The application contains two API endpoints:

- A home endpoint that returns a welcome message.
- An addition endpoint that accepts two integer query parameters and returns their sum.

A separate test file uses FastAPI's `TestClient` to send requests to these endpoints and verify their responses.

The tests validate both:

- HTTP status codes
- JSON response data

This provides a basic foundation for building more comprehensive automated test suites for FastAPI applications.

---

## 📂 Project Structure

```text
Pytest-24/
│
├── Pytest_main_24.py
├── Pytest_main_test.py
└── README.md
```

---

## 🚀 API Endpoints

### Home Endpoint

```http
GET /
```

### Example Response

```json
{
    "message": "Hello Lakshay"
}
```

---

### Addition Endpoint

```http
GET /add?a=5&b=3
```

### Example Response

```json
{
    "result": 8
}
```

---

## 🧪 Tests Included

### Home API Test

The test verifies:

```text
GET /
   ↓
Status Code = 200
   ↓
Response = {"message": "Hello Lakshay"}
```

### Add API Test

The test sends:

```text
GET /add?a=5&b=3
```

and verifies:

```text
Status Code = 200
Response = {"result": 8}
```

---

## 🔄 Testing Workflow

```text
FastAPI Application
        │
        ▼
     TestClient
        │
        ▼
 Send HTTP Request
        │
        ▼
 FastAPI Endpoint
        │
        ▼
 Receive Response
        │
        ▼
     Assertions
        │
   ┌────┴────┐
   ▼         ▼
Status      JSON
Code        Data
   │         │
   └────┬────┘
        ▼
   Test Passed ✅
```

---

## 📚 Features Demonstrated

- FastAPI `TestClient`
- Pytest test functions
- HTTP request simulation
- Status code assertions
- JSON response assertions
- Query parameter testing
- Automated API validation

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Create basic tests for FastAPI endpoints.
- Use `TestClient` to simulate API requests.
- Write assertions using Pytest.
- Validate HTTP status codes.
- Validate JSON response data.
- Separate application code from test code.
- Build the foundation for automated API testing.

---

## 🛠 Tech Stack

- Python
- FastAPI
- Pytest
- FastAPI TestClient
- Uvicorn

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.