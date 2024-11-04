from typing import Optional
from pydantic import BaseModel, EmailStr

# User model
class User(BaseModel):
    name: str
    email: EmailStr
    password: str

# Item model
# class Item(BaseModel):
#     title: str
#     description: Optional[str] = None
#     price: float
#     in_stock: bool = True
