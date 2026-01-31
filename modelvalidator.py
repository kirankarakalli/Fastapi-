from pydantic import BaseModel,EmailStr,field_validator,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    emergency: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    @model_validator(mode='after')
    def validate_emergency_detail(cls,model):
        if model.age>60 and 'emergency' not in model.emergency:
            raise ValueError('patients older than 60 must have emergency details')
        
        return model
    
def update_patient_into(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print('updated')

patient_info = {'name':'kiran', 'email':'abc@icici.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'emergency':{'phone':'2353462'}}


patient1=Patient(**patient_info)
update_patient_into(patient1)