import pytest
from sqlmodel import SQLModel, create_engine, Session
from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app

engine = create_engine(settings.TEST_DATABASE_URL, echo=True)

SQLModel.metadata.create_all(engine)


@pytest.fixture(scope="function")
def get_session():
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="function")
def test_client(get_session):
    def override_get_session():
        try:
            yield get_session
        finally:
            get_session.close()
    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def storage_payload():
    return {
        "id": 1,
        "name": "Склад Ozon",
        "capacity": 5000,
    }


@pytest.fixture()
def product_payload():
    return {
        "id": 1,
        "name": "Сникерс",
        "quantity": 20,
        "storage_id": 1,
    }


