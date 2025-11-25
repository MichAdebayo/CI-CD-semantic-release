# SQLModel not required directly in tests
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemResponse


def test_item_model_fields() -> None:
    item = Item(nom="Keyboard", prix=49.99)
    assert item.nom == "Keyboard"
    assert item.prix == 49.99


def test_item_schema_create_and_response() -> None:
    data = {"nom": "Mouse", "prix": 9.99}
    item_create = ItemCreate(**data)
    assert item_create.nom == "Mouse"
    assert item_create.prix == 9.99

    # Create a model instance and ensure ItemResponse validates it
    item = Item(id=1, **data)
    item_response = ItemResponse.model_validate(item)
    assert item_response.id == 1
    assert item_response.nom == "Mouse"
