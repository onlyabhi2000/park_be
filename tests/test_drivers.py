
import pytest
from fastapi.testclient import TestClient

def test_register_driver(client: TestClient):
    response = client.post("/drivers/", json={
        "name": "Test Driver",
        "license_plate": "TEST1234"
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Driver registered successfully"
    assert response.json()["data"]["name"] == "Test Driver"
    assert response.json()["data"]["license_plate"] == "TEST1234"

def test_fetch_driver(client: TestClient):
    response = client.post("/drivers/", json={
        "name": "Test Driver 2",
        "license_plate": "TEST5678"
    })
    driver_id = response.json()["data"]["id"]


    response = client.get(f"/drivers/{driver_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Driver fetch successfully"
    assert response.json()["data"]["name"] == "Test Driver 2"
    assert response.json()["data"]["license_plate"] == "TEST5678"
