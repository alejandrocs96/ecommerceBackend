from pydantic import BaseModel


class addressCreate(BaseModel):
    id : int
    id_user : int
    department : str
    city : str
    address : str
    address_comp : str
    is_principal : int


class addressResponse(BaseModel):
    id : int
    id_user : int
    department : str
    city : str
    address : str
    address_comp : str
    is_principal : int

    class config:
        orm_mode: True
