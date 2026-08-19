# Assignment 2 - Task 1: JSON API Route

## Objective

The objective of this task is to create a beginner-level Flask application that reads a JSON list from a backend file (`backend/data.json`) and returns it as a JSON response through the `/api` route.

## Project Structure

```text
Task-1/
├── app.py
├── requirements.txt
├── README.md
└── backend/
    └── data.json
```

## Installation

### 1. Create and Activate Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

Install Flask using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Flask application by running:

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

## Test API

Open your web browser or an API client (e.g. Curl, Postman, or Python script) and navigate to:

```text
http://127.0.0.1:5000/api
```

### Expected Response

The endpoint will display the JSON data loaded from `backend/data.json`:

```json
[
    {
        "id": 1,
        "name": "Rahul",
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Priya",
        "course": "Flask"
    },
    {
        "id": 3,
        "name": "Amit",
        "course": "MongoDB"
    }
]
```

### Error Responses

- **File Not Found (`404 Not Found`)**: If `backend/data.json` is missing:
  ```json
  {
      "error": "Data file not found"
  }
  ```
- **Invalid JSON (`500 Internal Server Error`)**: If `backend/data.json` contains malformed JSON:
  ```json
  {
      "error": "Invalid JSON format in data file"
  }
  ```
