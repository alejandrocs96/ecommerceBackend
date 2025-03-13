from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    id_order = Column(Integer, ForeignKey("order.id"))
    id_product = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer)
    total = Column(Integer)

    
    order = relationship("Order", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")
