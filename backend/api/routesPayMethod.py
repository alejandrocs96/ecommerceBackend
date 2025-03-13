from fastapi import APIRouter, HTTPException, status, Depends
from config.db import get_db
from sqlalchemy.orm import Session
from schemas.payMethod import PayMethodS, PayMethodResponse
from service import logicPayMethod
from utils.jwt_handler import verificar_token_jwt

routerPayMethod = APIRouter()

@routerPayMethod.post("/payMethod/add",response_model = PayMethodResponse ,status_code=status.HTTP_201_CREATED, dependencies=[Depends(verificar_token_jwt)])
async def add_payMethod(payMethod: PayMethodS,db: Session =  Depends(get_db)):
    payMethodResponse = logicPayMethod.add_payMehtod(payMethod,db)
    if not payMethodResponse:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error agregando metodo de pago.")
    return payMethodResponse

@routerPayMethod.get("/payMethod/getall", status_code=status.HTTP_201_CREATED, dependencies=[Depends(verificar_token_jwt)])
async def get_add_payMethods(db: Session =  Depends(get_db)):
    payMethodResponse = logicPayMethod.getPayMehtods(db)
    if not payMethodResponse:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error obteniendo metodos de pago.")
    return payMethodResponse

@routerPayMethod.get("/payMethod/getclients", status_code=status.HTTP_200_OK)
async def get_paymethodsClient(db: Session =  Depends(get_db)):
    payMethodResponse = logicPayMethod.getPayMehtodsUsers(db)
    if not payMethodResponse:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error obteniendo metodos de pago.")
    return payMethodResponse

@routerPayMethod.put("/payMethod/update",status_code=status.HTTP_200_OK, dependencies=[Depends(verificar_token_jwt)])
async def update_payMethod(payMethod: PayMethodS,db: Session =  Depends(get_db)):
    payMethodResponse = logicPayMethod.updatePayMethod(payMethod,db)
    if not payMethodResponse:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error actualizando metodo de pago.")
    return payMethodResponse

@routerPayMethod.put("/payMethod/delete/{id}",status_code=status.HTTP_200_OK, dependencies=[Depends(verificar_token_jwt)])
async def delete_payMethod(id,db: Session =  Depends(get_db)):
    payMethodResponse = logicPayMethod.deletePayMethod(id,db)
    if not payMethodResponse:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Metodo de pago eliminado.")
    return payMethodResponse