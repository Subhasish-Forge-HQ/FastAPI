# 🏥 FastAPI Patient Management System API

A simple REST API project built using FastAPI that manages patient records stored in a JSON file.
This project demonstrates API development, path parameters, query parameters, sorting, validation, and exception handling using FastAPI.

---

# 📌 Project Overview

The Patient Management System API allows users to:

* View patient details using Patient ID
* Sort patient records by age or name
* Handle invalid requests using HTTP exceptions
* Access automatic API documentation using Swagger UI

Patient data is stored in a local `patients.json` file and loaded dynamically whenever an API request is made.

---

# 🚀 Features

* FastAPI REST API
* Patient lookup by Patient ID
* Sorting functionality
* Query parameter validation
* HTTP error handling
* JSON file-based storage
* Swagger UI documentation
* Beginner-friendly backend project

---

# 🧠 Technologies Used

* Python
* FastAPI
* Uvicorn
* JSON

---

# 📁 Project Structure

```bash
project/
│
├── main.py
├── patients.json
├── README.md
```

---

# ⚙️ Installation

## 1️⃣ Create Virtual Environment

```bash
python -m venv myenv
```

---

## 2️⃣ Activate Virtual Environment

### Windows

```bash
myenv\Scripts\activate
```

---

## 3️⃣ Install Required Packages

```bash
pip install fastapi uvicorn
```

---

# ▶️ Run the FastAPI Server

```bash
uvicorn main:app --reload
```

---

# 🌐 Base URL

```bash
http://127.0.0.1:8000
```

---

# 📌 API Endpoints

| Method | Endpoint                 | Description         |
| ------ | ------------------------ | ------------------- |
| GET    | `/`                      | Home Route          |
| GET    | `/patients/{patient_id}` | Get patient details |
| GET    | `/sort`                  | Sort patients       |

---

# 🏠 Home Route

## Endpoint

```http
GET /
```

## Response

```json
{
  "message": "Patient Management System API"
}
```

---

# 👤 Get Patient Details

## Endpoint

```http
GET /patients/{patient_id}
```

## Example

```bash
http://127.0.0.1:8000/patients/P001
```

## Successful Response

```json
{
  "patient_id": "P001",
  "name": "Amit Kumar",
  "age": 34,
  "gender": "Male",
  "blood_group": "A+",
  "disease": "Diabetes",
  "phone": "9876543210",
  "address": "Ranchi, Jharkhand"
}
```

---

# ❌ Error Handling

If patient ID does not exist:

```json
{
  "detail": "patient is not found"
}
```

Status Code:

```bash
404 Not Found
```

---

# 🔄 Sort Patients API

This API sorts patient records by:

* age
* name

---

## Endpoint

```http
GET /sort
```

---

# Query Parameters

| Parameter | Description |
| --------- | ----------- |
| sort_by   | age or name |
| order     | asc or desc |

---

# Example URLs

## Sort by Age Ascending

```bash
http://127.0.0.1:8000/sort?sort_by=age&order=asc
```

---

## Sort by Age Descending

```bash
http://127.0.0.1:8000/sort?sort_by=age&order=desc
```

---

## Sort by Name Ascending

```bash
http://127.0.0.1:8000/sort?sort_by=name&order=asc
```

---

# ⚠️ Validation

The API validates:

* Valid sorting fields
* Correct sorting order

---

# Invalid Field Example

```bash
/sort?sort_by=height
```

## Response

```json
{
  "detail": "Invalid field. Select from ['age', 'name']"
}
```

---

# Invalid Order Example

```bash
/sort?sort_by=age&order=random
```

## Response

```json
{
  "detail": "Invalid order. Select between asc and desc"
}
```

---

# 🔍 Code Explanation

---

# 1️⃣ FastAPI App Initialization

```python
app = FastAPI()
```

Creates the FastAPI application.

---

# 2️⃣ Load JSON Data

```python
def load_data():
```

Reads patient data from `patients.json`.

The function converts the patient list into a dictionary using:

```python
patient_id
```

for faster searching.

---

# 3️⃣ Path Parameters

```python
Path(...)
```

Used for validating patient IDs in API routes.

---

# 4️⃣ Query Parameters

```python
Query(...)
```

Used for sorting options like:

* sort_by
* order

---

# 5️⃣ HTTPException

```python
HTTPException
```

Used for custom API error responses.

---

# 6️⃣ Sorting Logic

```python
sorted()
```

Sorts patient data dynamically using:

```python
lambda
```

function.

---

# 📘 Automatic API Documentation

FastAPI automatically generates API docs.

## Swagger UI

```bash
http://127.0.0.1:8000/docs
```

---

## ReDoc

```bash
http://127.0.0.1:8000/redoc
```

---

# 📦 Future Improvements

* Add new patient
* Update patient details
* Delete patient
* Use database (MySQL / MongoDB)
* Add authentication
* Deploy on cloud

---

# 👨‍💻 Author

Built for learning FastAPI backend development and REST API concepts.
