from fastapi import FastAPI,Path,HTTPException,Query
import json
app=FastAPI()

def read_json():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data

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