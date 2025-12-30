from datetime import datetime
from database.models import MovementType
from typing import TypedDict

class MovementCreate(TypedDict):
    product_id: int
    type: MovementType
    quantity: int
    note: str | None

class MovementUpdate(TypedDict, total=False):
    product_id: int
    type: MovementType
    quantity: int
    note: str | None

class MovementData(TypedDict):
    id: int
    product_id: int
    type: MovementType
    quantity: int
    date: datetime
    note: str | None
