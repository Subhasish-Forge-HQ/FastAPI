from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)

    return {p["patient_id"]: p for p in data}


@app.get("/")
def hello():
    return {'message': 'Patient Management System API'}


@app.get('/patients/{patient_id}')
def view_patient(
    patient_id: str = Path(
        ...,
        description='ID of patient in the DB',
        example='P001'
    )
):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(
        status_code=404,
        detail='patient is not found'
    )


@app.get('/sort')
def sort_patients(
    sort_by: str = Query(
        ...,
        description='Sort on the basis of age or name'
    ),
    order: str = Query(
        'asc',
        description='Sort in asc or desc order'
    )
):

    valid_fields = ['age', 'name']

    # FIXED CONDITION
    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f'Invalid field. Select from {valid_fields}'
        )

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400,
            detail='Invalid order. Select between asc and desc'
        )

    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data
