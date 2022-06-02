from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    id: Optional[int]
    name: str
    description: str
    price: int
    stars: int
    img: str
    location: str
    createdAt: datetime = datetime.now()
    updatedAt: Optional[datetime]
    typeid: int




class Item(BaseModel):
    typeId: Optional[int] 
    totalSize: int
    offset: int
    Products: Product | None = None