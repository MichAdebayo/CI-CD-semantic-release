# pytest import not required; tests use TestClient via fixtures
from fastapi.testclient import TestClient


def test_health_and_crud(app_client: TestClient) -> None:
    # Health
    r = app_client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"

    # Create
    payload = {"nom": "IntegrationKeyboard", "prix": 99.99}
    r = app_client.post("/items", json=payload)
    assert (
        r.status_code == 201
    ), f"POST /items failed: {r.status_code} {r.text} {r.json() if r.headers.get('content-type', '').startswith('application/json') else ''}"
    created = r.json()
    assert created["nom"] == "IntegrationKeyboard"
    assert created["prix"] == 99.99
    item_id = created["id"]

    # Get collection
    r = app_client.get("/items")
    assert r.status_code == 200
    items = r.json()
    assert any(i["id"] == item_id for i in items)

    # Get single
    r = app_client.get(f"/items/{item_id}")
    assert r.status_code == 200
    item = r.json()
    assert item["id"] == item_id

    # Update
    update_payload = {"prix": 79.99}
    r = app_client.put(f"/items/{item_id}", json=update_payload)
    assert (
        r.status_code == 200
    ), f"PUT /items/{item_id} failed: {r.status_code} {r.text} {r.json() if r.headers.get('content-type', '').startswith('application/json') else ''}"
    updated = r.json()
    assert updated["prix"] == 79.99

    # Delete
    r = app_client.delete(f"/items/{item_id}")
    assert r.status_code == 204

    # Not found afterwards
    r = app_client.get(f"/items/{item_id}")
    assert r.status_code == 404
