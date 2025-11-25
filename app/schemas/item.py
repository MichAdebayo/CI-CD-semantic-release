from sqlmodel import Field, SQLModel
from typing import Optional

class ItemBase(SQLModel):
    nom: str = Field(min_length=1, max_length=255)
    prix: float = Field(gt=0)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(SQLModel):
    nom: str | None = Field(None, min_length=1, max_length=255)
    prix: float | None = Field(None, gt=0)



class ItemResponse(ItemBase):
    id: int
