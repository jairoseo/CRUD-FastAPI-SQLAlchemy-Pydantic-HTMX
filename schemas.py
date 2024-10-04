from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name : str
    creation_date : Optional[datetime] = None
    amount : int
    price : int
    description : Optional[str] = None
    
class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int    
    
    model_config = ConfigDict(from_attributes=True)