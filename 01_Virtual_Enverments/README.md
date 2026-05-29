# FastAPI Beginner Project

## Create Virtual Environment

```bash
python -m venv myenv
```

This command creates a virtual environment folder named `myenv`.

---

## Activate Virtual Environment

### Windows

```bash
myenv\Scripts\activate
```

After activation, your terminal will show the virtual environment name.

---

## Install Required Packages

```bash
pip install fastapi uvicorn pydantic
```

### Packages Description

* **FastAPI** → Web framework for building APIs
* **Uvicorn** → ASGI server to run FastAPI
* **Pydantic** → Data validation library

---

# FastAPI Application Code

Create a file named `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message': 'Hello World'}

@app.get("/about")
def about():
    return {'message': 'I love this FastAPI'}
```

---

# Run the FastAPI Server

```bash
uvicorn main:app --reload
```

## Explanation

* `main` → Python file name (`main.py`)
* `app` → FastAPI instance name
* `--reload` → Automatically reloads the server after code changes

---

# Open in Browser

After running the server, open:

```bash
http://127.0.0.1:8000
```

### API Routes

| Route    | Description           |
| -------- | --------------------- |
| `/`      | Returns Hello World   |
| `/about` | Returns About Message |

---

# Automatic API Documentation

FastAPI automatically provides API docs.

## Swagger UI

```bash
http://127.0.0.1:8000/docs
```

## ReDoc

```bash
http://127.0.0.1:8000/redoc
```

---

# Output Example

## Home Route

```json
{
  "message": "Hello World"
}
```

## About Route

```json
{
  "message": "I love this FastAPI"
}
```

---

# Advantages of FastAPI

* Fast performance
* Easy to learn
* Automatic documentation
* Async support
* Data validation
* Modern Python framework

---

# Project Structure

```bash
project-folder/
│
├── myenv/
├── main.py
└── README.md
```
