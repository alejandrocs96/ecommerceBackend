from pydantic import BaseModel


class categoryRequest(BaseModel):
    id : int
    name : str
    description : str
    state : int
    position : int
    image : str

class categoryResponse(BaseModel):
    id : int
    name : str
    description : str
    state : int
    position : int
    image : str

    class config:
        orm_mode: True
