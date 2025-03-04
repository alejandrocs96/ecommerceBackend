from sqlalchemy.orm import Session
from schemas.category import categoryRequest
from model.category import Category
from fastapi import HTTPException

def add_category(category: categoryRequest ,db: Session):
    cont = db.query(Category).filter(Category.name == category.name).count()
    if cont > 0:
        raise HTTPException(status_code=400, detail="El nombre de categoria ya existe.")
    new_Category = Category(
        name = category.name,
        description = category.description,
        state = 1,
        position = category.position,
        image = category.image,
        
    )
    db.add(new_Category)
    db.commit()
    db.refresh(new_Category)
    return new_Category


def getCategoryCommerce(db: Session):
    listCategory = db.query(Category).filter(Category.state == 1).all()
    return {"code": 200, "details": listCategory}

def getCategoryAll(db: Session):
    listCategory = db.query(Category).all()
    return {"code": 200, "details": listCategory}

def delete_category(id: int,db: Session):
    try:
        db.query(Category).filter(Category.id == id).delete()
        db.commit()
        return {"code": 200, "details": "Categoria eliminada."}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error borrando Categoria")
    

def update_category(category: categoryRequest, db: Session):
    db.query(Category).filter(Category.id == category.id).update({
        Category.name : category.name,
        Category.description : category.description,
        Category.state : category.state,
        Category.position : category.position,
        Category.image : category.image
        })
    db.commit()
    return {"code": 200,"message": "Categoria actualizado."}