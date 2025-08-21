# routes/parking_slots.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from configuration.db import get_db
from schemas.parking_slot import ParkingSlotCreate, ParkingSlotUpdate, ParkingSlotOut
from services import parking_slot as svc
from utils.response import standard_response  # <-- your helper

router = APIRouter(prefix="/slots", tags=["Parking Slots"])

def _dump(slot) -> dict:
    return ParkingSlotOut.model_validate(slot).model_dump()

@router.post("/")
def create_slot(payload: ParkingSlotCreate, db: Session = Depends(get_db)):
    slot = svc.create_parking_slot(db, payload)
    return standard_response(201, "Parking slot created successfully", _dump(slot))

@router.get("/by-lot/{lot_id}")
def list_slots_by_lot(lot_id: int, db: Session = Depends(get_db)):
    slots = svc.get_slots_by_lot(db, lot_id)
    data = [_dump(s) for s in slots]
    return standard_response(200, "Slots fetched successfully", data)

@router.get("/by-lot/{lot_id}/available")
def list_available_slots(lot_id: int, db: Session = Depends(get_db)):
    slots = svc.get_available_slots(db, lot_id)
    data = [_dump(s) for s in slots]
    return standard_response(200, "Available slots fetched successfully", data)

@router.get("/{slot_id}")
def get_slot(slot_id: int, db: Session = Depends(get_db)):
    slot = svc.get_parking_slot(db, slot_id)
    if not slot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Slot not found")
    return standard_response(200, "Slot fetched successfully", _dump(slot))

@router.put("/{slot_id}")
def update_slot(slot_id: int, payload: ParkingSlotUpdate, db: Session = Depends(get_db)):
    slot = svc.update_parking_slot(db, slot_id, payload)
    if not slot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Slot not found")
    return standard_response(200, "Parking slot updated successfully", _dump(slot))

@router.delete("/{slot_id}")
def delete_slot(slot_id: int, db: Session = Depends(get_db)):
    ok = svc.delete_parking_slot(db, slot_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Slot not found")
    return standard_response(200, "Parking slot deleted successfully", {"id": slot_id})
