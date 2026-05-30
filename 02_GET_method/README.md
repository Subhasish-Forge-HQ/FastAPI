## 📝 Project Description

This project is a simple Patient Management System API developed using FastAPI.

The application stores patient records inside a JSON file (`patients_data.json`) and exposes API endpoints to access the data.

### What I Implemented

#### 1. FastAPI Application Initialization

```python
from fastapi import FastAPI

app = FastAPI()
```

Created a FastAPI application instance that serves as the entry point of the API.

---

#### 2. Loading Patient Data from JSON File

```python
import json

def load_data():
    with open('patients_data.json', 'r') as f:
        data = json.load(f)
    return data
```

Created a helper function that:

* Opens the JSON file
* Reads patient records
* Converts JSON data into Python objects
* Returns the patient data to API endpoints

---

#### 3. Home Endpoint

```python
@app.get("/")
def hello():
    return {'message':'Patient Management System API'}
```

Purpose:

* Provides a welcome message
* Confirms that the API is running successfully

---

#### 4. About Endpoint

```python
@app.get("/about")
def about():
    return {'message': 'A fully Functional API to manage Your Patient Record'}
```

Purpose:

* Describes the API
* Gives basic information about the project

---

#### 5. View Patient Records Endpoint

```python
@app.get('/view')
def view():
    data = load_data()
    return data
```

Purpose:

* Retrieves all patient records
* Returns the data stored in `patients_data.json`

---

## 📂 JSON Data Structure

Patient information is stored inside a JSON file.

Example:

```json
{
  "patients": [
    {
      "id": 1,
      "name": "Rahul Sharma",
      "age": 28,
      "gender": "Male",
      "disease": "Fever",
      "percentage_recovery": 85
    }
  ]
}
```

Each patient record contains:

| Field               | Description               |
| ------------------- | ------------------------- |
| id                  | Unique patient identifier |
| name                | Patient name              |
| age                 | Patient age               |
| gender              | Patient gender            |
| disease             | Disease diagnosed         |
| percentage_recovery | Recovery percentage       |

---

## 🔄 Project Workflow

1. User sends a request to the API.
2. FastAPI receives the request.
3. The `load_data()` function reads patient data from the JSON file.
4. Data is converted into Python objects.
5. API returns the response in JSON format.
6. User receives patient information through the endpoint.

---

## 🎯 Learning Outcomes

Through this project, I learned:

* FastAPI fundamentals
* API routing
* JSON file handling
* GET requests
* Returning JSON responses
* Building REST APIs using Python
* Working with API documentation using Swagger UI
