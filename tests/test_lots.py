
import pytest
from fastapi.testclient import TestClient


def test_create_lot(client: TestClient):
    response = client.post("/lots/", json={
        "name": "Test Lot",
        "address": "Test Location",
        "total_capacity": 100,
        "available_slots": 100
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Parking lot created successfully"
    assert response.json()["data"]["lot"]["name"] == "Test Lot"
