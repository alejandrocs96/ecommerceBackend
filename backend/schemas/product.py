from pydantic import BaseModel


class productRequest(BaseModel):
    id : int
    id_category : int
    name : str
    collection : str
    image : str
    description : str
    price : int
    price_offer : int
    state : int
    order: int

class productResponse(BaseModel):
    id : int
    id_category : int
    name : str
    collection : str
    image : str
    description : str
    price : int
    price_offer : int
    state : int
    order : int

    class config:
        orm_mode : True