from typing import Optional
from pydantic import BaseModel, field_validator
from schemas.cart import cartRequest
from datetime import date, datetime

class Order(BaseModel):
    
    id : int
    id_user : int
    id_address : int
    is_pay : int
    comments : str
    pay_method : int
    state : int
    subtotal: int
    total : int
    created : date
    cart : list[cartRequest]

    @field_validator("created", mode="before")
    def parse_created(cls, value):
        if isinstance(value, date):  # Si ya es date, no lo convierte
            return value
        if isinstance(value, str):  # Si es string, intenta convertirlo
            try:
                return datetime.strptime(value, "%d-%m-%Y").date()  # Ajusta según el formato recibido
            except ValueError:
                raise ValueError("Invalid date format. Expected DD-MM-YYYY.")
        raise ValueError("Invalid type for created. Expected date or string.")




class OrderResponse(BaseModel):
    id : int
    id_user : int
    id_address : int
    is_pay : int
    comments : str
    state : int
    subtotal: int
    pay_method : int
    total : int
    created : date
    cart : Optional[list[cartRequest]] = None

    