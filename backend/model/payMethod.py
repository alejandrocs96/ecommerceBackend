from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, func
from sqlalchemy.orm import relationship
from config.db import Base

class PayMethod(Base):
    __tablename__ = "payMethod"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60))
    state = Column(Integer, nullable=False)
    desc = Column(String(360))

    orders = relationship("Order", back_populates="payment")
