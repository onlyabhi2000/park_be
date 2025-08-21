# services/parking_slot.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.parking_slot import ParkingSlot
from models.parking_lot import ParkingLot
from schemas.parking_slot import ParkingSlotCreate, ParkingSlotUpdate

def _get_lot_or_404(db: Session, lot_id: int) -> ParkingLot:
    lot = db.query(ParkingLot).filter(ParkingLot.id == lot_id).first()
    if not lot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Parking lot not found")
    return lot

def create_parking_slot(db: Session, payload: ParkingSlotCreate) -> ParkingSlot:
    _get_lot_or_404(db, payload.lot_id)

    exists = (
        db.query(ParkingSlot)
        .filter(ParkingSlot.lot_id == payload.lot_id, ParkingSlot.slot_number == payload.slot_number)
        .first()
    )
    if exists:
        raise HTTPException(status_code=400, detail="slot_number already exists in this lot")

    slot = ParkingSlot(**payload.model_dump())
    db.add(slot)
    db.commit()
    db.refresh(slot)
    return slot

def get_slots_by_lot(db: Session, lot_id: int) -> list[ParkingSlot]:
    _get_lot_or_404(db, lot_id)
    return db.query(ParkingSlot).filter(ParkingSlot.lot_id == lot_id).all()

def get_available_slots(db: Session, lot_id: int) -> list[ParkingSlot]:
    _get_lot_or_404(db, lot_id)
    return (
        db.query(ParkingSlot)
        .filter(ParkingSlot.lot_id == lot_id, ParkingSlot.is_occupied.is_(False))
        .all()
    )

def get_parking_slot(db: Session, slot_id: int) -> ParkingSlot | None:
    return db.query(ParkingSlot).filter(ParkingSlot.id == slot_id).first()

def update_parking_slot(db: Session, slot_id: int, payload: ParkingSlotUpdate) -> ParkingSlot | None:
    slot = get_parking_slot(db, slot_id)
    if not slot:
        return None

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(slot, key, value)

    db.commit()
    db.refresh(slot)
    return slot

def delete_parking_slot(db: Session, slot_id: int) -> bool:
    slot = get_parking_slot(db, slot_id)
    if not slot:
        return False
    db.delete(slot)
    db.commit()
    return True
