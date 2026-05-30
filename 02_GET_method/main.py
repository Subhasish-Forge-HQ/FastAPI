from fastapi import FastAPI 
app = FastAPI ()

import json
def load_data():
    with open('patients_data.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return{'message':'Patient Management System API'}

@app.get("/about")
def about():
    return {'message': 'A fully Functional API to manage Your Patient Record'}
 
@app.get('/view')
def view():
    data = load_data()
    return data