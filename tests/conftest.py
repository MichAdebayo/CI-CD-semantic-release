from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.pool import StaticPool


@pytest.fixture(scope="session")
def engine() -> Generator:
    # Create an in-memory SQLite engine suitable for testing (shared between threads)
    sqlite_url = "sqlite:///:memory:"
    engine = create_engine(
        sqlite_url,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    # Ensure tables are created once for the test session
    SQLModel.metadata.create_all(engine)
    yield engine
    # teardown: drop tables
    SQLModel.metadata.drop_all(engine)


@pytest.fixture()
def session(engine) -> Generator:
    """Provide a session to be used within tests."""
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="function")
def app_client(monkeypatch, engine):
    """Provide an httpx AsyncClient using the project's FastAPI app but with the test engine.

    This monkeypatches app.database.engine so the app uses the in-memory DB for tests.
    """
    # Monkeypatch the engine used by the app
    import app.database as db_mod
    import importlib

    monkeypatch.setattr(db_mod, "engine", engine)

    # Import/reload app.main so lifespan uses the patched engine
    import app.main as app_main

    importlib.reload(app_main)

    # Create tables for each test function to ensure clean DB state
    SQLModel.metadata.create_all(engine)

    client = TestClient(app_main.app)

    yield client

    client.close()
    # Clean DB state
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
