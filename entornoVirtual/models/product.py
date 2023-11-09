from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(default="New Product", min_length=5, max_length=15)
    price: float = Field(default=0, ge=0, le=1000)
    stock: int = Field(default=0, gt=0)