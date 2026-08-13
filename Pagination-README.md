# API Pagination

This branch demonstrates how to implement **pagination** in a FastAPI endpoint while retrieving and processing data from an external website.

Pagination is used to divide a large collection of data into smaller, manageable sections. Instead of returning every available record in a single response, the API allows the client to specify which page and how many records should be returned.

---

## 📌 Concepts Covered

- API Pagination
- Query Parameters
- Page and Limit
- Pagination Logic
- Data Slicing
- Web Crawling
- BeautifulSoup
- External API Requests
- FastAPI Query Parameters

---

## 📖 Overview

This API demonstrates how pagination can be applied to data collected through web crawling.

The application retrieves news titles from **Hacker News** using:

- `requests` to fetch the webpage.
- `BeautifulSoup` to parse the HTML.
- CSS class selection to locate news titles.
- Python list slicing to implement pagination.

The endpoint accepts two query parameters:

- `page` — determines which page of results should be returned.
- `limit` — determines how many results should appear on each page.

---

## 🚀 API Endpoint

### Get Paginated News

```http
GET /news
```

### Query Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | `integer` | `1` | Page number to retrieve |
| `limit` | `integer` | `5` | Number of records per page |

---

## 📥 Example Requests

### First Page

```http
GET /news?page=1&limit=5
```

### Second Page

```http
GET /news?page=2&limit=5
```

### Ten Results Per Page

```http
GET /news?page=1&limit=10
```

---

## 📤 Example Response

```json
{
    "page": 1,
    "limit": 5,
    "total": 30,
    "data": [
        "News Title 1",
        "News Title 2",
        "News Title 3",
        "News Title 4",
        "News Title 5"
    ]
}
```

The actual news titles and total count depend on the content returned by Hacker News at the time of the request.

---

## 🔢 Pagination Logic

The pagination is implemented using Python list slicing.

### Starting Index

```python
start = (page - 1) * limit
```

### Ending Index

```python
end = start + limit
```

### Data Selection

```python
title[start:end]
```

For example:

```text
page = 1
limit = 5

start = (1 - 1) * 5
      = 0

end = 0 + 5
    = 5
```

Therefore:

```text
title[0:5]
```

returns the first five records.

For page 2:

```text
start = (2 - 1) * 5
      = 5

end = 5 + 5
    = 10
```

Therefore:

```text
title[5:10]
```

returns the next five records.

---

## 🔄 Pagination Workflow

```text
Client
   │
   │ GET /news?page=2&limit=5
   ▼
FastAPI
   │
   ▼
Fetch Hacker News
   │
   ▼
Parse HTML with BeautifulSoup
   │
   ▼
Extract News Titles
   │
   ▼
Calculate Pagination
   │
   ├── start = (page - 1) × limit
   │
   └── end = start + limit
   │
   ▼
Slice Data
   │
   ▼
Return Paginated Response
```

---

## 📚 Features Demonstrated

- FastAPI application setup
- `@app.get()` decorator
- Query parameters
- Default parameter values
- External HTTP requests
- Web crawling
- BeautifulSoup HTML parsing
- List slicing
- Pagination calculations
- Structured JSON responses

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Implement pagination using FastAPI query parameters.
- Use `page` and `limit` to control returned data.
- Calculate pagination offsets.
- Slice collections using Python.
- Combine web crawling with API pagination.
- Return structured paginated responses.

---

## 🛠 Tech Stack

- Python
- FastAPI
- Requests
- BeautifulSoup4
- Uvicorn

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.