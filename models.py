from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class ProductModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    creation_date = Column(DateTime, default=datetime.now)
    amount = Column(Integer)
    price = Column(Integer)
    description = Column(String)