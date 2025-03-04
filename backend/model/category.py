from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.db import Base

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False)
    description = Column(String(200))
    state = Column(Integer, nullable=False)
    position = Column(Integer, nullable=False)
    image = Column(String)
    
    products = relationship("Product", back_populates="category")
