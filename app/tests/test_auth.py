
import pytest
from fastapi.testclient import TestClient



def test_register_owner(client: TestClient):
    response = client.post("/auth/register/owner", json={
        "name": "Test Owner",
        "email": "testowner@example.com",
        "password": "password"
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Owner registered successfully"


def test_register_attendant(client: TestClient):
    response = client.post("/auth/register/attendant", json={
        "name": "Test Attendant",
        "email": "testattendant@example.com",
        "password": "password",
        "owner_id": 1
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Attendant registered successfully"


def test_login_owner(client: TestClient):
    # First, register an owner to ensure the owner exists
    client.post("/auth/register/owner", json={
        "name": "Test Owner Login",
        "email": "testownerlogin@example.com",
        "password": "password"
    })

    # Now, attempt to login
    response = client.post("/auth/login", json={
        "email": "testownerlogin@example.com",
        "password": "password"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"
    assert "access_token" in response.json()["data"]
