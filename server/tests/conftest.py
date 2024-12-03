import pytest
from fastapi.testclient import TestClient
from server.main import app

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client 