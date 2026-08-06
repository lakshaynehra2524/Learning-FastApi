# CORS Handling

This branch demonstrates how to configure **Cross-Origin Resource Sharing (CORS)** in FastAPI to enable secure communication between a frontend application and a backend API.

Modern web applications often have the frontend and backend running on different origins (domains, ports, or protocols). Without proper CORS configuration, browsers block cross-origin requests for security reasons. FastAPI provides built-in middleware to manage these permissions.

---

## 📌 Concepts Covered

- Cross-Origin Resource Sharing (CORS)
- CORS Middleware
- Allowed Origins
- HTTP Methods
- Request Headers
- Frontend–Backend Communication
- React & FastAPI Integration

---

## 📖 Overview

This project demonstrates how to enable CORS in a FastAPI application and establish communication with a React frontend.

The backend application:

- Configures CORS middleware.
- Allows requests from a specified frontend origin.
- Enables credentials such as cookies or authorization headers.
- Permits all HTTP methods.
- Permits all request headers.

A sample React application is also included to demonstrate frontend-to-backend communication running on separate local development servers.

This setup provides the foundation for integrating FastAPI APIs with modern frontend frameworks such as React, Vue, or Angular.

---

## 🚀 API Endpoint

### Home Endpoint

```
GET /
```

---

## 📤 Example Response

```json
{
    "message": "CORS ENABLE API"
}
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `CORSMiddleware`
- `add_middleware()`
- Allowed Origins
- Allowed Methods
- Allowed Headers
- Credentials Support
- Cross-Origin API Communication

---

## 🌐 Project Structure

```text
CORSHandling-22/
│
├── main.py                 # FastAPI Backend
├── my-react-app/           # React Frontend
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
└── README.md
```

---

## 🔄 Frontend–Backend Workflow

```
React Frontend
(http://localhost:5173)
        │
        │ HTTP Request
        ▼
FastAPI Backend
(http://127.0.0.1:8000)
        │
        │ CORS Middleware Validation
        ▼
Request Allowed ✅
        │
        ▼
API Response Returned
```

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Configure CORS in FastAPI.
- Enable communication between React and FastAPI.
- Restrict API access to trusted origins.
- Configure allowed HTTP methods and headers.
- Build frontend-backend applications that communicate securely across different origins.

---

## 🛠 Tech Stack

- Python
- FastAPI
- CORSMiddleware
- React
- JavaScript
- Vite
- Uvicorn

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.