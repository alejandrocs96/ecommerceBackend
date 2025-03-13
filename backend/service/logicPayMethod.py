from sqlalchemy.orm import Session
from schemas.payMethod import PayMethodS
from model.payMethod import PayMethod
from fastapi import HTTPException


def add_payMehtod(payMethod: PayMethodS,db: Session):
    cont = db.query(PayMethod).filter(PayMethod.name == payMethod.name).count()
    if cont > 0:
        raise HTTPException(status_code=400, detail="Ya existe un metodo de pago con ese nombre.")
    new_pay = PayMethod(
        name = payMethod.name,
        desc = payMethod.desc,
        state = payMethod.state
    )
    db.add(new_pay)
    db.commit()
    db.refresh(new_pay)
    return new_pay



def getPayMehtodsUsers(db: Session):
    listPaymets = db.query(PayMethod).filter(PayMethod.state == 1).all()
    return {"code": 200, "details": listPaymets}

def getPayMehtods(db: Session):
    listPaymets = db.query(PayMethod).filter(PayMethod != 3).all()
    return {"code": 200, "details": listPaymets}

def deletePayMethod(id: int,db: Session):
    try:
        db.query(PayMethod).filter(PayMethod.id == id).update({
            PayMethod.state : 3
        })
        db.commit()
        return {"code": 200, "details": "Metodo de pago eliminado."}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error borrando metodo de pago.")

def updatePayMethod(payMethod: PayMethodS,db: Session):
    cont = db.query(PayMethod).filter(PayMethod.name == payMethod.name).count()
    if cont > 0:
        raise HTTPException(status_code=400, detail="Ya existe un metodo de pago con ese nombre.")
    db.query(PayMethod).filter(PayMethod.id == payMethod.id).update({
            PayMethod.name : payMethod.name,
            PayMethod.desc : payMethod.desc,
            PayMethod.state : payMethod.state
        })
    db.commit()
    return {"code": 200,"message": "Metodo de pago actualizado."}