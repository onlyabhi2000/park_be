from sqlalchemy.orm import Session
from models.parking_lot import ParkingLot
from schemas.lots import ParkingLotCreate

def create_lot_service(payload: ParkingLotCreate, owner, db: Session):
    lot = ParkingLot(
        name=payload.name,
        address=payload.address,
        total_capacity=payload.total_capacity,
        available_slots=payload.available_slots,
        owner_id=owner.id,
    )
    db.add(lot)
    db.commit()
    db.refresh(lot)
    return lot
