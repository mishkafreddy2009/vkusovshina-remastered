from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "hello"


def test_read_storages():
    response = client.get("/api/storages/")
    assert response.json() == []
