from fastapi.testclient import TestClient

from app.api import api

client = TestClient(api)


def test_add_endpoint():
    response = client.get("/add", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_health():
    assert client.get("/health").json() == {"status": "ok"}
