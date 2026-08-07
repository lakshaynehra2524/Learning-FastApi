# Environment Variables & Configuration Management

This branch demonstrates how to manage **application configuration** using **Environment Variables (.env)** in FastAPI.

Hardcoding sensitive information such as secret keys, database URLs, and application settings is not recommended in production applications. Instead, environment variables provide a secure and flexible way to manage configuration across different environments such as development, testing, and production.

---

## 📌 Concepts Covered

- Environment Variables
- `.env` File
- Configuration Management
- `python-dotenv`
- Application Settings
- Secure Configuration
- FastAPI Configuration

---

## 📖 Overview

This project demonstrates how to separate application configuration from source code using a `.env` file and a dedicated configuration module.

The application includes:

- Loading environment variables from a `.env` file.
- Centralizing configuration inside a `config.py` module.
- Accessing configuration values throughout the application.
- Configuring CORS origins using environment variables.
- Keeping sensitive information outside the source code.

This approach improves maintainability, enhances security, and makes it easy to deploy the same application across multiple environments without modifying the codebase.

---

## 📂 Project Structure

```text
Env_var-23/
│
├── Env_var-23.py      # FastAPI Application
├── config.py          # Configuration Loader
├── .env               # Environment Variables
└── README.md
```

---

## 🔧 Environment Variables

Example `.env` configuration:

```env
ORIGINS=http://localhost:5173

SECRET_KEY=mysecretkey

DB_URL=sqlite:///./test.db
```

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
- Environment Variables
- `.env` File
- `python-dotenv`
- Configuration Module
- CORS Middleware
- Secure Application Configuration

---

## 🔄 Configuration Workflow

```text
.env File
     │
     ▼
python-dotenv
     │
     ▼
config.py
     │
     ▼
Settings Object
     │
     ▼
FastAPI Application
     │
     ▼
Application Configuration
```

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Store application settings in a `.env` file.
- Load environment variables using `python-dotenv`.
- Create a centralized configuration module.
- Access configuration values throughout a FastAPI project.
- Separate configuration from application logic.
- Build applications that are easier to deploy across multiple environments.

---

## 🛠 Tech Stack

- Python
- FastAPI
- python-dotenv
- CORSMiddleware
- Uvicorn

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.