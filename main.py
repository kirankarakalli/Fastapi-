from fastapi import FastAPI,Path,HTTPException,Query
from pydantic import BaseModel,computed_field,Field
from fastapi.responses import JSONResponse
from typing import List,Annotated,Dict,Literal
import json

app=FastAPI()

class Patient(BaseModel):
    id: Annotated[str,Field(...,description='Id of the patient',Example=['P001'])]
    name: Annotated[str,Field(...,description='name of the patient')]
    city: Annotated[str,Field(...,description='name of the city')]
    age: Annotated[int,Field(...,gt=1,lt=120,description='age of patient')]
    gender: Annotated[Literal['male','female','others'],Field(...,description='gender of patient')]
    height: Annotated[float,Field(...,description='height of the patient')]
    weight: Annotated[float,Field(...,description='weight of the patient')]


    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return 'UnderWeight'
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi<30:
            return 'overweight'
        else:
            return 'obesce'

def read_json():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.get("/")
def hello():
    return {'message':'Hello world'}

@app.get("/about")
def about():
    return {'messgae':'welcome to AI field'}


@app.get('/view')
def viewdata():
    data=read_json()

    return data

@app.get('/patient/{id}')
def patient(id:str=Path(...,description='ID of the patient in the DB',example='P001')):
    data=read_json()

    if id in data:
        return data[id]
    
    raise HTTPException(status_code=404,detail='patient not found')


@app.get('/sort')
def sort_patients(sort_by:str=Query(...,description='sort on the basis of height,weight and bmi'),order:str=Query('asc',description='sort in asc or desc order')):
    valid_fields=['heights','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail='Invalid field select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order select bw asc and desc')
    
    data=read_json()
    sorted_data=sorted(data.values(),key=lambda x:x.get('sort_by',0),reverse=False)
    return sorted_data


@app.post('/create')
def create_patient(patient:Patient):
    data=read_json()

    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient already exists')
    
    data[patient.id]=patient.model_dump(exclude=['id'])
    save_data(data)
    return JSONResponse(status_code=201,content={'message':'patient created successfully'})

