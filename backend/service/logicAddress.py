from sqlalchemy.orm import Session
from schemas.address import addressCreate
from model.address import Address
from fastapi import HTTPException


def add_address(address: addressCreate,db: Session):
    cont = db.query(Address).filter(Address.id_user == address.id_user).count()
    if cont >= 3:
        raise HTTPException(status_code=400, detail="Solo puede crear como maximo 3 direcciones diferentes.")
    db.query(Address).filter(Address.id_user == address.id_user).update({
        Address.is_principal : 2
    }, synchronize_session="fetch")
    new_address = Address(
        id_user = address.id_user,
        department = address.department,
        city = address.city,
        address = address.address,
        address_comp = address.address_comp,
        is_principal = 1
    )
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


def getAddress(id_user: int,db: Session):
    listAddress = db.query(Address).filter(Address.id_user == id_user).all()
    return {"code": 200, "details": listAddress}

def deleteAddress(id: int,db: Session):
    try:
        db.query(Address).filter(Address.id == id).delete()
        db.commit()
        return {"code": 200, "details": "Direccion eliminada."}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error borrando direccion")
    

def getAddressDetail(id: int,db: Session):
    address = db.query(Address).filter(Address.id == id).first()
    return address

def updateAddress(address: addressCreate,db: Session):
    db.query(Address).filter(Address.id == address.id).update({
        Address.department : address.department,
        Address.city : address.city,
        Address.address : address.address,
        Address.address_comp : address.address_comp,
        Address.is_principal : address.is_principal
        })
    db.commit()
    return {"code": 200,"message": "Datos actualizado."}