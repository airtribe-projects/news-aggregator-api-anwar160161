from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_register():

    response = client.post(
        "/register",
        json={
            "username": "anwar",
            "email": "anwar@test.com",
            "password": "Password123"
        }
    )

    assert response.status_code in [200, 400]


def test_login():

    response = client.post(
        "/login",
        json={
            "email": "anwar@test.com",
            "password": "Password123"
        }
    )

    assert response.status_code == 200


def test_search_news():

    response = client.get(
        "/news/search?q=technology"
    )

    assert response.status_code == 200