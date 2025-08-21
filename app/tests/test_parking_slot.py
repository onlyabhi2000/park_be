import pytest
from fastapi.testclient import TestClient
from models.parking_lot import ParkingLot
from sqlalchemy.orm import Session
from models.parking_slot import ParkingSlot
from app.main import app
from configuration.db import get_db

client = TestClient(app)


@pytest.fixture
def db():
    from configuration.db import SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def create_parking_lot(db: Session):
    lot = ParkingLot(
        name="Test Lot",
        location="Test City",
        capacity=50
    )
    db.add(lot)
    db.commit()
    db.refresh(lot)
    return lot


def test_create_parking_slot_success(create_parking_lot):
    response = client.post(
        "/parking-slots/",
        json={
            "slot_number": "A1",
            "lot_id": create_parking_lot.id,
            "row_identifier": "R1",
            "is_handicap_accessible": True,
            "distance_from_exit": 5,
            "slot_size": "standard"
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["status_code"] == 201
    assert data["message"] == "Parking slot created successfully"
    assert data["data"]["slot_number"] == "A1"


def test_create_parking_slot_invalid_lot():
    response = client.post(
        "/parking-slots/",
        json={
            "slot_number": "B1",
            "lot_id": 9999,
            "row_identifier": "R2",
            "is_handicap_accessible": False,
            "distance_from_exit": 10,
            "slot_size": "large"
        },
    )
    assert response.status_code == 400
    data = response.json()
    assert data["status_code"] == 400
    assert data["message"] == "Parking lot does not exist"


def test_get_all_parking_slots(create_parking_lot):

    client.post(
        "/parking-slots/",
        json={
            "slot_number": "C1",
            "lot_id": create_parking_lot.id,
            "row_identifier": "R3",
            "is_handicap_accessible": False,
            "distance_from_exit": 7,
            "slot_size": "compact"
        },
    )

    response = client.get(f"/parking-slots/lot/{create_parking_lot.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status_code"] == 200
    assert isinstance(data["data"], list)
    assert len(data["data"]) >= 1
    assert data["data"][0]["lot_id"] == create_parking_lot.id


def test_get_parking_slot_by_id(create_parking_lot):
    """Fetch parking slot by ID."""
    slot_resp = client.post(
        "/parking-slots/",
        json={
            "slot_number": "D1",
            "lot_id": create_parking_lot.id,
            "row_identifier": "R4",
            "is_handicap_accessible": True,
            "distance_from_exit": 3,
            "slot_size": "standard"
        },
    )
    slot_id = slot_resp.json()["data"]["id"]

    response = client.get(f"/parking-slots/{slot_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status_code"] == 200
    assert data["data"]["id"] == slot_id


def test_get_invalid_slot_id():
    """Try fetching a non-existing slot."""
    response = client.get("/parking-slots/9999")
    assert response.status_code == 404
    data = response.json()
    assert data["status_code"] == 404
    assert data["message"] == "Parking slot not found"


def test_update_parking_slot(create_parking_lot):
    """Update slot details."""
    # Create slot
    slot_resp = client.post(
        "/parking-slots/",
        json={
            "slot_number": "E1",
            "lot_id": create_parking_lot.id,
            "row_identifier": "R5",
            "is_handicap_accessible": False,
            "distance_from_exit": 6,
            "slot_size": "compact"
        },
    )
    slot_id = slot_resp.json()["data"]["id"]

    response = client.put(
        f"/parking-slots/{slot_id}",
        json={
            "row_identifier": "R5-updated",
            "distance_from_exit": 12
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status_code"] == 200
    assert data["message"] == "Parking slot updated successfully"
    assert data["data"]["row_identifier"] == "R5-updated"


def test_delete_parking_slot(create_parking_lot):
    """Delete parking slot."""
    # Create slot
    slot_resp = client.post(
        "/parking-slots/",
        json={
            "slot_number": "F1",
            "lot_id": create_parking_lot.id,
            "row_identifier": "R6",
            "is_handicap_accessible": False,
            "distance_from_exit": 8,
            "slot_size": "standard"
        },
    )
    slot_id = slot_resp.json()["data"]["id"]

    response = client.delete(f"/parking-slots/{slot_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status_code"] == 200
    assert data["message"] == "Parking slot deleted successfully"

    # Verify deletion
    get_response = client.get(f"/parking-slots/{slot_id}")
    assert get_response.status_code == 404
