from sqlmodel import Field, SQLModel
from typing import Optional

class Item(SQLModel, table=True):
    __tablename__ = "items"

    id: int | None = Field(default=None, primary_key=True)
    nom: str = Field(index=True)
    prix: float

    def _legacy_method(self):
        pass
