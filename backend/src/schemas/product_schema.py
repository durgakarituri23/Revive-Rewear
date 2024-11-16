from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import Any

class ProductCreate(BaseModel):
    product_name: str
    description: str
    price: float

class ProductResponse(ProductCreate):
    id: str
    images: List[str] = []

class UpdateProductRequest(BaseModel):
    isApproved: bool


class  UpdateProductDetails(BaseModel):
  product_name: str
  description: str
  price: float