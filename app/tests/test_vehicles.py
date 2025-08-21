
import pytest
from fastapi.testclient import TestClient

def test_register_vehicle(client: TestClient):
    # First, register a driver to associate with the vehicle
    driver_response = client.post("/drivers/", json={
        "name": "Test Driver for Vehicle",
        "license_plate": "VEHICLE1"
    })
    driver_id = driver_response.json()["data"]["id"]

    response = client.post("/vehicles/", json={
        "make": "Test Make",
        "model": "Test Model",
        "color": "Test Color",
        "license_plate": "VEHICLE1",
        "driver_id": driver_id
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Vehicle registered sucessfuly"
    assert response.json()["data"]["make"] == "Test Make"
    assert response.json()["data"]["model"] == "Test Model"

def test_fetch_vehicle(client: TestClient):
    # First, register a driver and a vehicle to ensure they exist
    driver_response = client.post("/drivers/", json={
        "name": "Test Driver for Vehicle 2",
        "license_plate": "VEHICLE2"
    })
    driver_id = driver_response.json()["data"]["id"]

    vehicle_response = client.post("/vehicles/", json={
        "make": "Test Make 2",
        "model": "Test Model 2",
        "color": "Test Color 2",
        "license_plate": "VEHICLE2",
        "driver_id": driver_id
    })
    vehicle_id = vehicle_response.json()["data"]["id"]

    # Now, fetch the vehicle
    response = client.get(f"/vehicles/{vehicle_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Vehicle fetched successfully"
    assert response.json()["data"]["make"] == "Test Make 2"
    assert response.json()["data"]["model"] == "Test Model 2"
