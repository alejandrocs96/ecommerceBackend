from fastapi import APIRouter, HTTPException, status, Depends
from config.db import get_db
from sqlalchemy.orm import Session
from schemas.address import addressCreate, addressResponse
from service import logicAddress
from utils.jwt_handler import verificar_token_jwt


routerAddress = APIRouter()


@routerAddress.post("/address/create",response_model = addressResponse ,status_code=status.HTTP_201_CREATED, dependencies=[Depends(verificar_token_jwt)])
async def add_address(address: addressCreate, db: Session =  Depends(get_db)):
    try:
        return logicAddress.add_address(address=address, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@routerAddress.get("/address/getall/{id}",status_code=status.HTTP_200_OK, dependencies=[Depends(verificar_token_jwt)])
async def get_address(id: int, db: Session =  Depends(get_db)):
    try:
        return logicAddress.getAddress(id_user=id, db=db)
    except Exception as e:
        return HTTPException(status_code=500, detail="Error en la insercion de la direccion")
    
@routerAddress.get("/address/get/{id}",response_model = addressResponse ,status_code=status.HTTP_200_OK, dependencies=[Depends(verificar_token_jwt)])
async def get_address(id: int, db: Session =  Depends(get_db)):
    try:
        return logicAddress.getAddressDetail(id, db=db)
    except Exception as e:
        return HTTPException(status_code=500, detail="Error en la insercion de la direccion")

@routerAddress.delete("/address/delete/{id}",status_code=status.HTTP_200_OK, dependencies=[Depends(verificar_token_jwt)])
async def get_address(id: int, db: Session =  Depends(get_db)):
    try:
        return logicAddress.deleteAddress(id, db=db)
    except Exception as e:
        return HTTPException(status_code=500, detail="Error en la insercion de la direccion")
    
@routerAddress.put("/address/update",status_code=status.HTTP_200_OK, dependencies=[Depends(verificar_token_jwt)])
async def get_address(address: addressCreate, db: Session =  Depends(get_db)):
    try:
        return logicAddress.updateAddress(address=address, db=db)
    except Exception as e:
        return HTTPException(status_code=500, detail="Error en la insercion de la direccion")