from sqlalchemy.orm import Session
from schemas.order import Order
from schemas.cart import cartRequest
from model.order import Order
from model.product import Product
from model.cart import Cart
from fastapi import HTTPException


def getProductsCart(id, db: Session):
    result = db.query(Cart).join(Product).filter(Cart.id_order == id).all()
    return { "code": 200, "data": result }


def add_order(order: Order, db: Session):
    
    new_order = Order(
        id_user = order.id_user,
        id_address = order.id_address,
        is_pay = order.is_pay,
        pay_method = order.pay_method,
        comments = order.comments,
        state = order.state,
        subtotal = order.subtotal,
        total = order.total
    )
    db.add(new_order)
    db.commit() 
    db.refresh(new_order)
    # save objects to cart
    for cart in order.cart:
        new_cart = Cart(
            id_order = new_order.id,
            id_product = cart.id_product,
            quantity = cart.quantity, 
            total = cart.total
        )
        db.add(new_cart)
    db.commit()

    return new_order
