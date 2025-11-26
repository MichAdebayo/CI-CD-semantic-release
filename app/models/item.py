from sqlmodel import Field, SQLModel
from typing import ClassVar


class Item(SQLModel, table=True):
    __tablename__: ClassVar[str] = "items"

    id: int | None = Field(default=None, primary_key=True)
    nom: str = Field(index=True)
    prix: float
