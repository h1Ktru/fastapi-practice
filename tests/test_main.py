import pytest
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (10, 20, 30),
        (-5, 3, -2),
        (0, 0, 0),
    ],
)
# 1+2=3、10+20=30、-5+3=-2、0+0=0
def test_add(a, b, expected):
    response = client.get(f"/add?a={a}&b={b}")

    assert response.status_code == 200
    assert response.json() == {"result": expected}


def test_add_invalid_parameter():
    response = client.get("/add?a=abc&b=5")

    assert response.status_code == 422