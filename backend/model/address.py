from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id"))
    department = Column(String(40), nullable=False)
    city = Column(String(40), nullable=False)
    address = Column(String(60), nullable=False)
    address_comp = Column(String(360))
    is_principal = Column(Integer, nullable=False)

    # Relación con Users
    user = relationship("Users", back_populates="addresses")