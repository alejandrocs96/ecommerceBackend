from pydantic import BaseModel, EmailStr

class userLogin(BaseModel):
    email: EmailStr
    password: str

class userCreate(BaseModel):
    id: int
    name : str
    last_name : str
    phone : str
    email : EmailStr
    password : str
    permission: int

class userResponse(BaseModel):
    id: int
    name: str
    last_name : str
    email: EmailStr
    phone: str
    permission: int

    class Config:
        orm_mode: True

class passwordChange(BaseModel):
    id: int
    lastPass: str
    newPass: str
