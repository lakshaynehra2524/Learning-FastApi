# Third-Party API Integration

This branch demonstrates how to integrate an external **third-party REST API** with a FastAPI application using Python's `requests` library.

Third-party API integration allows a backend application to consume data or functionality provided by external services and expose it through its own API endpoints.

---

## 📌 Concepts Covered

- Third-Party API Integration
- External REST APIs
- HTTP GET Requests
- Python `requests` Library
- API Response Handling
- Path Parameters
- HTTP Status Codes
- `HTTPException`
- JSON Responses

---

## 📖 Overview

This branch demonstrates how a FastAPI application can communicate with an external API and return its data to the client.

The application integrates with the **JSONPlaceholder** API and provides endpoints for:

- Fetching all posts.
- Fetching a specific post using its ID.

The FastAPI server sends an HTTP request to the external API using the `requests` library, receives the response, and returns the JSON data to the client.

The application also checks the response status code when retrieving a specific post. If the requested resource is not found, FastAPI raises an appropriate HTTP exception.

---

## 🚀 API Endpoints

### Get All Posts

```http
GET /posts
```

This endpoint requests all posts from the external API and returns the received JSON data.

---

### Get Single Post

```http
GET /posts/{post_id}
```

This endpoint accepts a post ID as a path parameter and requests the corresponding post from the external API.

Example:

```http
GET /posts/1
```

---

## 📤 Example Response

For:

```http
GET /posts/1
```

the API returns the JSON response received from the third-party service.

Example:

```json
{
    "userId": 1,
    "id": 1,
    "title": "Example post title",
    "body": "Example post content"
}
```

---

## 📤 Example Error Response

If the requested post does not exist:

```json
{
    "detail": "Page not found !"
}
```

**Status Code**

```text
404 Not Found
```

---

## 🔄 Third-Party API Workflow

```text
Client
   │
   │ GET /posts/1
   ▼
FastAPI Application
   │
   │ requests.get()
   ▼
External API
   │
   │ JSON Response
   ▼
FastAPI Application
   │
   │ Validate Response
   ▼
Client
```

---

## 📚 Features Demonstrated

- FastAPI application setup
- `@app.get()` decorator
- Path Parameters
- `requests.get()`
- External API communication
- JSON response handling
- HTTP status code checking
- `HTTPException`
- Third-party API consumption

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Consume an external REST API from FastAPI.
- Send HTTP GET requests using Python.
- Handle JSON responses from third-party services.
- Pass path parameters to external API requests.
- Handle unsuccessful API responses.
- Expose external API data through your own FastAPI endpoints.

---

## 🛠 Tech Stack

- Python
- FastAPI
- Requests
- JSONPlaceholder
- Uvicorn

---

