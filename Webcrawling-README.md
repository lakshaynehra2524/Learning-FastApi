# Web Crawling with FastAPI

This branch demonstrates how to perform basic **web crawling** using Python and integrate the crawling functionality into a FastAPI application.

Web crawling allows an application to retrieve information from web pages and extract specific content from the returned HTML. In this tutorial, the application fetches news-related content from an external website and extracts article titles using HTML parsing.

---

## 📌 Concepts Covered

- Web Crawling
- HTTP Requests
- HTML Parsing
- BeautifulSoup
- `requests` Library
- CSS Class Selection
- Data Extraction
- FastAPI Integration
- JSON Responses

---

## 📖 Overview

This API demonstrates how to retrieve and extract information from a web page using Python.

The application performs the following workflow:

- Sends an HTTP GET request to a target website.
- Receives the HTML response.
- Parses the HTML using BeautifulSoup.
- Searches for specific HTML elements using their CSS class.
- Extracts article titles from the matching elements.
- Returns the extracted titles through a FastAPI endpoint.

The branch also contains an initial example demonstrating the basic process of retrieving a webpage and accessing its HTML title using BeautifulSoup.

---

## 🚀 API Endpoint

### Get News

```http
GET /news
```

This endpoint fetches news-related content from the configured website and returns the extracted article titles.

---

## 📤 Example Response

```json
{
    "news": [
        "News Article Title 1",
        "News Article Title 2",
        "News Article Title 3"
    ]
}
```

The actual results depend on the content and HTML structure of the target website at the time of the request.

---

## 🔄 Web Crawling Workflow

```text
FastAPI Request
      │
      ▼
GET /news
      │
      ▼
Send HTTP Request
      │
      ▼
Target Website
      │
      ▼
HTML Response
      │
      ▼
BeautifulSoup
      │
      ▼
Find Target HTML Elements
      │
      ▼
Extract Article Titles
      │
      ▼
Return JSON Response
```

---

## 📚 Features Demonstrated

- FastAPI application setup
- `@app.get()` decorator
- HTTP requests using `requests`
- HTML parsing using BeautifulSoup
- Finding HTML elements with CSS classes
- Extracting text from HTML elements
- Returning scraped data as JSON

---

