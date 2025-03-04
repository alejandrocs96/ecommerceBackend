from fastapi import APIRouter, HTTPException, status, Depends
from utils.jwt_handler import verificar_token_jwt
from sqlalchemy.orm import Session
from schemas.product import productRequest, productResponse
from config.db import get_db
from service import logicProduct

routerProduct = APIRouter()

@routerProduct.post("/product/create",response_model = productResponse ,status_code=status.HTTP_201_CREATED, dependencies=[Depends(verificar_token_jwt)])
async def add_Product(product: productRequest, db: Session =  Depends(get_db)):
    try:
        return logicProduct.add_product(product = product, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@routerProduct.get("/product/commerce/{id}", status_code=status.HTTP_200_OK)
async def get_all_Product(id:int ,db: Session =  Depends(get_db)):
    try:
        return logicProduct.getProductsCommerce(id_category = id, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@routerProduct.get("/product/all", status_code=status.HTTP_200_OK, dependencies= [Depends(verificar_token_jwt)])
async def get_all_Product(db: Session =  Depends(get_db)):
    try:
        return logicProduct.getProductAll(db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@routerProduct.get("/product/detail/{id}", status_code=status.HTTP_200_OK)
async def get_all_Product(id:int, db: Session =  Depends(get_db)):
    try:
        return logicProduct.getProductsDetail(id = id,db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@routerProduct.put("/product/update" ,status_code=status.HTTP_201_CREATED, dependencies=[Depends(verificar_token_jwt)])
async def update_Product(product: productRequest, db: Session =  Depends(get_db)):
    try:
        return logicProduct.update_product(product = product, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@routerProduct.delete("/product/delete/{id}",status_code=status.HTTP_200_OK, dependencies=[Depends(verificar_token_jwt)])
async def delete_Product(id : int, db: Session =  Depends(get_db)):
    try:
        return logicProduct.delete_product(id=id, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
