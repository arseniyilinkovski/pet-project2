from typing import Optional

from pydantic import BaseModel


class UserAdd(BaseModel):
    username: str
    password: str
    email: Optional[str] = None


class User(UserAdd):
    id: int
    role: str


class UserId(BaseModel):
    ok: bool
    user_id: int


class ItemsAdd(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class Items(ItemsAdd):
    item_id: int


class ItemsID(BaseModel):
    ok: bool
    user_id: int
