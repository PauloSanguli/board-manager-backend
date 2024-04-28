"""class props of traffic-agent"""

from pydantic import BaseModel, EmailStr




class AccountProps(BaseModel):
    username: str
    password: str
    cellphone: str
    email: EmailStr

class Login(BaseModel):
    password: str
    email: EmailStr
