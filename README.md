# RAG 101

## Overview

RAG 101 is a basic FastAPI backend template designed for building AI applications.

The current backend provides:

* FastAPI server setup
* API key authentication
* Health check endpoint
* File upload handling
* Request/Response validation
* Separation of API and business logic

This backend will later be extended into a complete RAG pipeline.

---

# Project Structure

```
RAG-101/
│
├── main.py
├── core.py
├── models.py
├── requirements.txt
├── .env
└── uploads/
```

---

# Files

## main.py

The main entry point of the FastAPI application.

Responsibilities:

* Creates FastAPI app
* Loads environment variables
* Handles API authentication
* Defines API endpoints
* Handles file uploads
* Connects API requests with core logic

### Available Endpoints

| Endpoint   | Method | Description          |
| ---------- | ------ | -------------------- |
| `/`        | GET    | Check backend status |
| `/health`  | GET    | Health check         |
| `/upload`  | POST   | Upload files         |
| `/process` | POST   | Process input data   |

---

## models.py

Contains Pydantic models used for request and response validation.

### ProcessRequest

Input model:

```json
{
    "text": "Hello World"
}
```

### ProcessResponse

Output model:

```json
{
    "result": "Done"
}
```

---

## core.py

Contains the main application logic.

Currently:

```python
def process(data):
    return "Done"
```

This file will later contain the RAG pipeline:

```
Query
 |
Embedding
 |
FAISS Search
 |
Retrieve Context
 |
LLM Response
```

---

## requirements.txt

Contains required Python packages.

Current dependencies:

```
fastapi
uvicorn
```

---

## .env

Stores environment variables.

Example:

```
API_KEY=your_secret_key
```

Sensitive values should not be committed to GitHub.

---

# Authentication

Protected endpoints require an API key.

Header:

```
X-API-Key: your_secret_key
```

Used for:

* `/upload`
* `/process`

---

# Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start server:

```bash
uvicorn main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

# Current Architecture

```
Client
  |
  |
FastAPI
  |
  |
main.py
  |
  |
core.py
  |
  |
Response
```

---

# Future RAG Extension

The backend will be extended with:

```
Document Upload
        |
        |
Document Parser
        |
        |
Chunking
        |
        |
Embeddings
        |
        |
FAISS Vector Database
        |
        |
Semantic Search
        |
        |
Ollama LLM
        |
        |
Final Response
```

---

# Status

Completed:

✅ FastAPI Backend
✅ API Authentication
✅ Upload Endpoint
✅ Health Endpoint
✅ Request/Response Models

Upcoming:

* Document Processing
* Chunking
* Embeddings
* FAISS Integration
* RAG Pipeline
* LLM Integration
