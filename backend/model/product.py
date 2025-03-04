from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    id_category = Column(Integer, ForeignKey("category.id"))
    name = Column(String(60), nullable=False)
    collection = Column(String(60))
    image = Column(Text)
    description = Column(String(600))
    price = Column(Integer, nullable=False)
    price_offer = Column(Integer, nullable=True)
    state = Column(Integer, nullable=False)
    order = Column(Integer, nullable=False)

    category = relationship("Category", back_populates="products")
    cart_items = relationship("Cart", back_populates="product")
