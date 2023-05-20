import pytest
from fastapi.testclient import TestClient
from main import app
from main import database


@pytest.fixture(scope="module")
def test_app():
    app.dependency_overrides[database] = database
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module")
async def db():
    await database.connect()
    yield
    await database.disconnect()
