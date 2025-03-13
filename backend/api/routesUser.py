from fastapi import APIRouter, HTTPException, status, Depends, Response, Request
from config.db import get_db
from sqlalchemy.orm import Session
from schemas.users import userCreate, userResponse, userLogin, passwordChange
from service import logicUsers
from utils.jwt_handler import verificar_token_jwt
routerUser = APIRouter()

#check
@routerUser.post("/login", status_code=status.HTTP_200_OK)
async def loggin_user(response: Response, user: userLogin,db: Session =  Depends(get_db)):
    token = logicUsers.login_user(user,db)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Correo o contraseña incorrecto")
     
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="None",
        secure=True,
        path="/"  # Puedes probar con "None" si usas HTTPS y dominios diferentes
    )

    payload = verificar_token_jwt(token)

    return {"message": "Login exitoso"}


@routerUser.get("/session", status_code=status.HTTP_200_OK)
async def session_user(request: Request):
    dt = request.cookies.get("access_token")
    print(dt)
    if dt is None:
        raise HTTPException(status_code=401, detail="No autorizado")
    session = logicUsers.session_user(request.cookies.get("access_token"))
    if not session:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Correo o contraseña incorrecto")
    return session


@routerUser.post("/logout", status_code=status.HTTP_200_OK)
async def logout(response: Response):
    response.set_cookie(
        key="access_token",
        value="",
        expires=0,
        httponly=True,
        samesite="None",
        secure=True,
        path=""  # Puedes probar con "None" si usas HTTPS y dominios diferentes
    )
    return {"message": "Logout exitoso"}

#check
@routerUser.post("/users/create", response_model=userResponse, status_code=status.HTTP_201_CREATED)
async def add_user(user: userCreate,db: Session =  Depends(get_db)):
    return logicUsers.create_user(user= user, db =  db)

        
@routerUser.get("/users/all", status_code= status.HTTP_200_OK) # type: ignore
async def get_users(request:Request, page: int , page_size: int, db: Session =  Depends(get_db)):
    token = request.cookies.get("access_token")
    if token is None:
        raise HTTPException(status_code=401, detail="No autorizado")
    usuario = verificar_token_jwt(token)
    if usuario is None:
        raise HTTPException(status_code=401, detail="No autorizado 2")
    if page < 1 or page_size < 1:
        raise HTTPException(status_code=400, detail="Página y tamaño deben ser mayores que 0")
    try:
        return logicUsers.get_all_users(page= page, page_size=page_size,db =  db)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@routerUser.put("/users/update", status_code= status.HTTP_200_OK)
async def update_user(request: Request, user: userCreate, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if token is None:
        raise HTTPException(status_code=401, detail="No autorizado")
    usuario = verificar_token_jwt(token)
    if usuario is None:
        raise HTTPException(status_code=401, detail="No autorizado 2")
    try:
        response = logicUsers.update_user(user = user, db = db)
        return HTTPException(status_code=200, detail=response)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@routerUser.put("/users/changepassword", status_code= status.HTTP_200_OK)
async def change_password(request: Request, user: passwordChange, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if token is None:
        raise HTTPException(status_code=401, detail="No autorizado")
    usuario = verificar_token_jwt(token)
    if usuario is None:
        raise HTTPException(status_code=401, detail="No autorizado 2")
    try:
        response = logicUsers.update_password(user = user, db = db)
        return HTTPException(status_code=200, detail=response)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
