from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.db import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    phone = Column(String(30))
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    permission = Column(Integer, nullable=False)

    # Relación corregida
    orders = relationship("Order", back_populates="user")
    addresses = relationship("Address", back_populates="user")