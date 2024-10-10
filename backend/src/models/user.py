from pydantic import BaseModel, EmailStr

class User(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    password: str 


