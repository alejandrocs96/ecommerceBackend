from fastapi import APIRouter, HTTPException, status, Depends
from config.db import get_db
from sqlalchemy.orm import Session
from schemas.users import userCreate, userResponse, userLogin, passwordChange
from service import logicUsers
from utils.jwt_handler import verificar_token_jwt

routerUser = APIRouter()

@routerUser.post("/login", status_code=status.HTTP_200_OK)
async def loggin_user(user: userLogin,db: Session =  Depends(get_db)):
    token = logicUsers.login_user(user,db)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Correo o contraseña incorrecto")
    return {"access_token": token, "token_type": "bearer"}

@routerUser.post("/users/create", response_model=userResponse, status_code=status.HTTP_201_CREATED)
async def add_user(user: userCreate,db: Session =  Depends(get_db)):
    try: 
        return logicUsers.create_user(user= user, db =  db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
@routerUser.get("/users/all", dependencies=[Depends(verificar_token_jwt)], status_code= status.HTTP_200_OK) # type: ignore
async def get_users(page: int , page_size: int, db: Session =  Depends(get_db)):
    try: 
        if page < 1 or page_size < 1:
            raise HTTPException(status_code=400, detail="Página y tamaño deben ser mayores que 0")
        return logicUsers.get_all_users(page= page, page_size=page_size,db =  db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@routerUser.put("/users/update", dependencies=[Depends(verificar_token_jwt)], status_code= status.HTTP_200_OK)
async def update_user(user: userCreate, db: Session = Depends(get_db)):
    try:
        response = logicUsers.update_user(user = user, db = db)
        return HTTPException(status_code=200, detail=response)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@routerUser.put("/users/changepassword", status_code= status.HTTP_200_OK)
async def change_password(user: passwordChange, db: Session = Depends(get_db)):
    try:
        response = logicUsers.update_password(user = user, db = db)
        return HTTPException(status_code=200, detail=response)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
