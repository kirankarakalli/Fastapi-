from pydantic import BaseModel,EmailStr,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
def update_patient_into(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print('updated')

patient_info = {'name':'kiran', 'email':'abc@icici.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'contact_details':{'phone':'2353462'}}


patient1=Patient(**patient_info)
update_patient_into(patient1)