from pydantic import BaseModel


class cartRequest(BaseModel):
    id : int
    id_order : int
    id_product : int

class cartResponse(BaseModel):
    id : int
    id_order : int
    id_product : int