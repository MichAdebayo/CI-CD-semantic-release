from sqlalchemy.pool import StaticPool
from sqlmodel import SQLModel, Session, create_engine
import pytest

from app.services.item_service import ItemService
from app.schemas.item import ItemCreate, ItemUpdate

# app.models.item.Item imported via schemas and services; explicit import removed


@pytest.fixture
def test_engine():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    yield engine
    SQLModel.metadata.drop_all(engine)
    # Dispose engine to ensure underlying sqlite connections are closed
    from contextlib import suppress

    with suppress(Exception):
        engine.dispose()


@pytest.fixture
def db_session(test_engine):
    with Session(test_engine) as session:
        yield session


def test_create_and_get_item(db_session: Session) -> None:
    data = ItemCreate(nom="Keyboard", prix=59.99)
    created = ItemService.create(db_session, data)
    assert created.id is not None
    assert created.nom == "Keyboard"
    assert created.prix == 59.99

    fetched = ItemService.get_by_id(db_session, created.id)
    assert fetched is not None
    assert fetched.nom == "Keyboard"


def test_update_item(db_session: Session) -> None:
    data = ItemCreate(nom="Screen", prix=199.99)
    created = ItemService.create(db_session, data)
    assert created.id is not None
    item_id = created.id

    update_data = ItemUpdate(nom="Remote Control", prix=149.99)
    updated = ItemService.update(db_session, item_id, update_data)
    assert updated is not None
    assert updated.prix == 149.99


def test_delete_item(db_session: Session) -> None:
    data = ItemCreate(nom="SSD", prix=79.99)
    created = ItemService.create(db_session, data)
    assert created.id is not None
    assert ItemService.delete(db_session, created.id) is True
    # second delete returns False
    assert ItemService.delete(db_session, created.id) is False


def test_get_all_empty(db_session: Session) -> None:
    items = ItemService.get_all(db_session)
    assert items == []


def test_get_by_id_not_found(db_session: Session) -> None:
    assert ItemService.get_by_id(db_session, 9999) is None


def test_update_nonexistent_returns_none(db_session: Session) -> None:
    update_data = ItemUpdate(nom=None, prix=10.0)
    assert ItemService.update(db_session, 9999, update_data) is None


def test_delete_nonexistent_returns_false(db_session: Session) -> None:
    assert ItemService.delete(db_session, 9999) is False
