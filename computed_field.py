from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    emergency: Dict[str,str]
    weight: float
    height:float

    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=round((self.weight/self.height**2),2)

    
def update_patient_into(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.calculate_bmi)
    print('updated')

patient_info = {'name':'kiran', 'email':'abc@icici.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'height':1.76,'emergency':{'phone':'2353462'}}


patient1=Patient(**patient_info)
update_patient_into(patient1)