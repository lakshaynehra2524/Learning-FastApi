# File Uploads & Static File Serving

This branch demonstrates how to implement **file uploading** and **static file serving** in FastAPI.

Many real-world applications require users to upload files such as images, documents, PDFs, or profile pictures. FastAPI provides built-in support for handling multipart file uploads and serving uploaded files through static routes.

---

## 📌 Concepts Covered

- File Uploads
- Multipart Form Data
- Static File Serving
- File Storage
- Directory Management
- File Validation
- HTTP Exceptions

---

## 📖 Overview

This API demonstrates the complete workflow of uploading and accessing files using FastAPI.

The application performs the following operations:

- Creates an upload directory automatically.
- Accepts files through a multipart POST request.
- Stores uploaded files on the local filesystem.
- Serves uploaded files as static resources.
- Generates accessible URLs for uploaded files.
- Validates file existence before returning file URLs.

This tutorial introduces the basic file management workflow commonly used in web applications before integrating cloud storage services such as AWS S3 or Azure Blob Storage.

---

## 🚀 API Endpoints

### Upload File

```
POST /upload
```

**Request Body**

| Field | Type | Description |
|-------|------|-------------|
| `file` | UploadFile | File to upload |

---

### Get File URL

```
GET /files/{filename}
```

---

### Home Endpoint

```
GET /
```

---

## 📤 Example Upload Response

```json
{
    "message": "File Uploaded successfully",
    "fileName": "resume.pdf",
    "file_url": "http://127.0.0.1:8000/files/resume.pdf"
}
```

---

## 📤 Example File URL Response

```json
{
    "file_url": "http://127.0.0.1:8000/files/resume.pdf"
}
```

---

## 📤 Example Error Response

```json
{
    "detail": "File not found"
}
```

**Status Code**

```
404 Not Found
```

---

## 📚 FastAPI Features Demonstrated

- `FastAPI()` application instance
- `@app.post()` decorator
- `@app.get()` decorator
- `UploadFile`
- `File`
- `StaticFiles`
- File System Operations
- Directory Creation
- File Storage
- HTTP Exceptions

---

## 📂 File Upload Workflow

```
Client
   │
   │ Select File
   ▼
POST /upload
   │
   ▼
FastAPI Server
   │
   │ Validate File
   ▼
Save File to Upload Directory
   │
   ▼
Generate File URL
   │
   ▼
Return Upload Response
   │
   ▼
GET /files/{filename}
   │
   ▼
Serve Static File
```

---

## 🎯 Learning Outcome

After completing this tutorial, you will understand how to:

- Upload files using FastAPI.
- Handle multipart form-data requests.
- Store uploaded files on the local filesystem.
- Serve static files using `StaticFiles`.
- Generate accessible URLs for uploaded files.
- Build the foundation for file management APIs.

---

## 🛠 Tech Stack

- Python
- FastAPI
- Uvicorn
- StaticFiles
- UploadFile
- shutil
- os

---

## 📂 Branch Purpose

This branch is part of my **FastAPI Learning** repository, where each branch represents an individual tutorial. Every branch focuses on a specific FastAPI concept, creating a structured, chapter-wise learning journey from fundamentals to production-ready API development.