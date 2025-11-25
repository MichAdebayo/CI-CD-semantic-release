from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    __tablename__: str = "items"

    id: int | None = Field(default=None, primary_key=True)
    nom: str = Field(index=True)
    prix: float

    def _legacy_method(self):
        pass
