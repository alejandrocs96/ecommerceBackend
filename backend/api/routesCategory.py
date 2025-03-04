from fastapi import APIRouter, HTTPException, status, Depends
from utils.jwt_handler import verificar_token_jwt
from sqlalchemy.orm import Session
from schemas.category import categoryRequest, categoryResponse
from config.db import get_db
from service import logicCategory

routerCategory = APIRouter()

@routerCategory.post("/category/create",response_model = categoryResponse ,status_code=status.HTTP_201_CREATED, dependencies=[Depends(verificar_token_jwt)])
async def add_category(category: categoryRequest, db: Session =  Depends(get_db)):
    try:
        return logicCategory.add_category(category = category, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@routerCategory.get("/category/all", status_code=status.HTTP_200_OK, dependencies=[Depends(verificar_token_jwt)])
async def get_all_category(db: Session =  Depends(get_db)):
    try:
        return logicCategory.getCategoryAll(db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@routerCategory.get("/category/allcommerce", status_code=status.HTTP_200_OK)
async def get_all_category(db: Session =  Depends(get_db)):
    try:
        return logicCategory.getCategoryCommerce(db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@routerCategory.put("/category/update" ,status_code=status.HTTP_201_CREATED, dependencies=[Depends(verificar_token_jwt)])
async def update_category(category: categoryRequest, db: Session =  Depends(get_db)):
    try:
        return logicCategory.update_category(category = category, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@routerCategory.delete("/category/delete/{id}",status_code=status.HTTP_201_CREATED, dependencies=[Depends(verificar_token_jwt)])
async def delete_category(id : int, db: Session =  Depends(get_db)):
    try:
        return logicCategory.delete_category(id=id, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
