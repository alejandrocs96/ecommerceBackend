# utils/jwt_handler.py
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from dotenv import load_dotenv
import os
load_dotenv()
# Clave secreta para firmar el JWT
SECRET_KEY = os.getenv('SECRET_KEY_TOKEN')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_HOURS = 36

# Esquema de autenticación para leer el token JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Función para crear token JWT
def create_jwt(data: dict):
    payload = data.copy()
    # Expira en 1 hora
    payload["exp"] = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    # Crea el token
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Función para verificar y decodificar el JWT
def verify_jwt(token: str):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded
    except jwt.ExpiredSignatureError:
        return None  # Token expirado
    except jwt.JWTError:
        return None  # Token inválido

# Dependencia para verificar el token en rutas protegidas
def verificar_token_jwt(token: str = Depends(oauth2_scheme)):
    try:
        # Decodificar el token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario = payload.get("email")
        id = payload.get("user_id")
        name = payload.get("name")
        index = payload.get("index")
        if usuario is None:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token no válido",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token no válido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"email": usuario, "id": id, "name": name, "index": index}