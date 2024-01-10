from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    quantity: int


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    id: int
    checked: bool


class ItemRead(ItemBase):
    id: int
    checked: bool

    class Config:
        from_attributes = True
