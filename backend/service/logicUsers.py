from model.users import Users
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from schemas.users import userCreate, userLogin, passwordChange
from utils.utils import get_password_hash, verify_password
from utils.jwt_handler import create_jwt, verificar_token_jwt



def login_user(userLogin: userLogin ,db: Session):
    db_user = db.query(Users).filter(Users.email == userLogin.email).first()
    if not db_user or not verify_password(userLogin.password, db_user.password):
        raise HTTPException(status_code=400,detail= "Correo o contraseña incorrectos.") 
    # Generar token JWT
    token = create_jwt({"user_id": db_user.id, "email": db_user.email, "name": db_user.name, "index": db_user.permission}) 
    return token

def session_user(session):
    session = verificar_token_jwt(session)
    if not session:
        raise HTTPException(status_code=400,detail= "Sesión no válida.")
    
    return session


def create_user(user: userCreate, db: Session):
    # Verificar si el correo ya existe
    existing_user = db.query(Users).filter( Users.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail= "El correo ya está registrado.")
    
    # Crear usuario con contraseña cifrada
    db_user = Users(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        phone= user.phone, 
        password=get_password_hash(user.password),
        permission= user.permission 
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(page: int, page_size: int, db: Session):
    total = db.query(func.count(Users.id)).scalar()
    offset = (page - 1) * page_size
    users_consult = db.query(Users).offset(offset).limit(page_size).all()

    return {"page" : page,
        "page_size" : page_size,
        "total" : total,
        "usuarios" : users_consult }

def update_user(user: userCreate, db: Session):
    db.query(Users).filter(Users.id == user.id).update({
        Users.name : user.name,
        Users.last_name : user.last_name,
        Users.permission : user.permission,
        Users.phone : user.phone
    })
    db.commit()
    return {"code": 200,"message": "Datos actualizado."}

def update_password(user: passwordChange, db: Session):
    db_user = db.query(Users).filter(Users.id == user.id).first()
    if verify_password( user.lastPass,db_user.password):
        db.query(Users).filter(Users.id == user.id).update({
            Users.password : get_password_hash(user.newPass)
        })
        db.commit()
        return {"code": 200, "message": "Contraseña actualizada."}
    raise HTTPException(status_code=400, detail="La contraseña no coincide.")
