from fastapi import APIRouter, HTTPException, status, Depends
from config.db import get_db
from sqlalchemy.orm import Session
from schemas.order import OrderResponse, Order
from service import logicOrder
from utils.jwt_handler import verificar_token_jwt
from service import logicOrder #, update_order


routerOrder = APIRouter()

@routerOrder.post("/order/create",response_model = OrderResponse ,status_code=status.HTTP_201_CREATED, dependencies=[Depends(verificar_token_jwt)])
async def add_Order(order: Order, db: Session =  Depends(get_db)):
    try:
        return logicOrder.add_order(order = order, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@routerOrder.get("/order/cart/{id}", status_code=status.HTTP_200_OK, dependencies=[Depends(verificar_token_jwt)])
async def get_cart(id: int, db: Session =  Depends(get_db)):
    try:
        return logicOrder.getProductsCart(id = id, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@routerOrder.put("/order/update",response_model = OrderResponse ,status_code=status.HTTP_200_OK, dependencies=[Depends(verificar_token_jwt)])
async def update_order(order: Order, db: Session =  Depends(get_db)):
    try:
        return logicOrder.update_order(order = order, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    