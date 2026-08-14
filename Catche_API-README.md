# API Caching

This branch demonstrates how to implement a basic **in-memory caching mechanism** in a FastAPI application.

Caching allows an application to temporarily store previously retrieved data and reuse it for subsequent requests instead of repeatedly fetching the same data from an external source.

---

## 📌 Concepts Covered

- API Caching
- In-Memory Cache
- Cache Expiration
- Cache Refresh
- External API Requests
- Web Crawling
- Performance Measurement
- FastAPI API Endpoints
- Global Variables

---

## 📖 Overview

This API demonstrates a simple time-based caching strategy for externally retrieved data.

The application fetches news titles from **Hacker News** and stores the results in memory.

Instead of making an external request for every `/news` request, the application checks when the data was last fetched.

### Cache Behavior

- If the cached data is **older than 60 seconds**, fresh data is fetched.
- If the cached data is **less than 60 seconds old**, the existing cached data is returned.
- The time taken to process the request is also measured and returned.

This reduces unnecessary external requests and demonstrates the basic principle behind caching systems.

---

## 🚀 API Endpoint

### Get News

```http
GET /news
```

The endpoint returns the first five cached news titles.

---

## 📤 Example Response

```json
{
    "time_taken": 0.0021,
    "data": [
        "News Article 1",
        "News Article 2",
        "News Article 3",
        "News Article 4",
        "News Article 5"
    ]
}
```

The actual news content and request time will vary.

---

## ⏱️ Cache Expiration

The application uses a **60-second cache expiration period**.

```python
if time.time() - last_fetch > 60:
```

This means:

```text
Request
   │
   ▼
Check Cache Age
   │
   ├── Less than 60 sec
   │       │
   │       ▼
   │   Use Cached Data
   │
   └── More than 60 sec
           │
           ▼
      Fetch Fresh Data
           │
           ▼
       Update Cache
```

---

## 🔄 Caching Workflow

```text
Client
   │
   │ GET /news
   ▼
FastAPI
   │
   ▼
Check Cache
   │
   ├─────────────── Cache Valid ───────────────┐
   │                                           │
   │                                           ▼
   │                                    Return Cached Data
   │
   └────────────── Cache Expired ──────────────┐
                                               │
                                               ▼
                                      Fetch Hacker News
                                               │
                                               ▼
                                      Parse HTML
                                               │
                                               ▼
                                      Update Cache
                                               │
                                               ▼
                                      Return New Data
```

---

## 📊 Performance Measurement

The API measures how long the request takes:

```python
start = time.time()

# API processing

end = time.time()

time_taken = round(end - start, 4)
```

This makes it possible to compare the performance of:

```text
Fresh Data Request
        vs
Cached Data Request
```

Typically, the cached request should require significantly less processing because it avoids the external HTTP request and HTML parsing.

---

## 📚 Features Demonstrated

- FastAPI application setup
- In-memory data storage
- Global cache variables
- Time-based cache expiration
- External HTTP requests
- Web scraping with BeautifulSoup
- Cache refresh logic
- Performance measurement
- JSON responses

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Implement a basic in-memory cache.
- Store API results temporarily.
- Set a cache expiration period.
- Refresh stale cached data.
- Reduce repeated external API requests.
- Measure API execution time.
- Understand the basic performance benefits of caching.

---

