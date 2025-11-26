def test_root_and_lifespan(app_client):
    # This will exercise the app lifespan startup and the root handler
    r = app_client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Items CRUD API"}


def test_update_and_delete_missing_returns_404(app_client):
    # Use an ID that does not exist and ensure routes return 404
    missing_id = 999999

    # Attempt to update missing item
    r = app_client.put(f"/items/{missing_id}", json={"prix": 1.23})
    assert r.status_code == 404

    # Attempt to delete missing item
    r = app_client.delete(f"/items/{missing_id}")
    assert r.status_code == 404


def test_lifespan_executes(engine):
    """Directly execute the async lifespan context to ensure startup runs.

    Running the async context ensures `SQLModel.metadata.create_all(engine)`
    inside `lifespan` is executed and covered by tests.
    """
    import asyncio
    from app.main import lifespan, app
    from sqlmodel import SQLModel

    async def _run():
        # Ensure clean state so create_all in lifespan does work
        SQLModel.metadata.drop_all(engine)
        async with lifespan(app):
            # inside lifespan: tables should be created
            pass

    asyncio.run(_run())
