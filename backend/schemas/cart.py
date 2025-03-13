from pydantic import BaseModel


class cartRequest(BaseModel):
    id : int
    id_order : int
    id_product : int
    quantity : int
    total : int

class cartResponse(BaseModel):
    id : int
    id_order : int
    id_product : int
    quantity : int
    total : int