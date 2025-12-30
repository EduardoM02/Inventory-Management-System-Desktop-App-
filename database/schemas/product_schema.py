from datetime import datetime
from decimal import Decimal
from typing import TypedDict

class ProductCreate(TypedDict):
    name: str
    description: str | None
    category_id: int
    stock: int
    price: Decimal

class ProductUpdate(TypedDict, total=False):
    name: str
    description: str | None
    category_id: int
    stock: int
    price: Decimal

class ProductData(TypedDict):
    id: int
    name: str
    description: str | None
    category_id: int
    stock: int
    price: Decimal
    created_at: datetime