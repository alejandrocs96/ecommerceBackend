from pydantic import BaseModel


class PayMethodS(BaseModel):
    id : int
    name : str
    state : int
    desc : str

    class Config:
        orm_mode = True

class PayMethodResponse(BaseModel):
    id : int
    name : str
    state : int
    desc : str