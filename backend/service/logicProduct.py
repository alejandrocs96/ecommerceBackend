from sqlalchemy.orm import Session
from sqlalchemy import and_
from schemas.product import productRequest
from model.product import Product
from fastapi import HTTPException

def add_product(product: productRequest ,db: Session):
    cont = db.query(Product).filter(Product.name == product.name).count()
    if cont > 0:
        raise HTTPException(status_code=400, detail="El nombre de producto ya existe.")
    new_product = Product(
        id_category = product.id_category,
        name =  product.name,
        collection = product.collection,
        image =  product.image,
        description =  product.description,
        price = product.price,
        price_offer = product.price_offer,
        state = product.state ,
        order =  product.order
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def getProductsCommerce(id_category: int,db: Session):
    listCategory = db.query(Product).filter(and_(Product.state == 1, Product.id_category == id_category)).all()
    return {"code": 200, "details": listCategory}

def getProductsDetail(id: int,db: Session):
    listCategory = db.query(Product).filter(Product.id == id).all()
    return {"code": 200, "details": listCategory}

def getProductAll(db: Session):
    listCategory = db.query(Product).all()
    return {"code": 200, "details": listCategory}

def delete_product(id: int,db: Session):
    try:
        db.query(Product).filter(Product.id == id).delete()
        db.commit()
        return {"code": 200, "details": "Producto eliminada."}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error borrando Product")
    

def update_product(product: productRequest, db: Session):
    db.query(Product).filter(Product.id == product.id).update({
        Product.id_category : product.id_category,
        Product.name : product.name,
        Product.collection : product.collection,
        Product.description : product.description,
        Product.state : product.state,
        Product.order : product.order,
        Product.price : product.price,
        Product.price_offer : product.price_offer,
        Product.image : product.image
        })
    db.commit()
    return {"code": 200,"message": "Categoria actualizado."}
