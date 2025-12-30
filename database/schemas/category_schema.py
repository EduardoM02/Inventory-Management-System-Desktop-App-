from typing import TypedDict

class CategoryCreate(TypedDict):
    name: str
    description: str

class CategoryUpdate(TypedDict, total=False):
    name: str
    description: str

class CategoryData(TypedDict):
    id: int
    name: str
    description: str