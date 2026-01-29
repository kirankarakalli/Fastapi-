from fastapi import FastAPI
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