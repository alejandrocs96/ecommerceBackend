from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, func
from sqlalchemy.orm import relationship
from config.db import Base

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id"))
    id_address = Column(Integer, ForeignKey("address.id"))
    is_pay = Column(Boolean, default=False)
    comments = Column(String(360))
    state = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)
    created = Column(Date, default=func.current_date(), nullable=False)

    user = relationship("Users", back_populates="orders")
    cart_items = relationship("Cart", back_populates="order")
