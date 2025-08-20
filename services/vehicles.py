from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.vehicle import Vehicle
from models.driver import Driver
from schemas.vehicles import VehicleCreate

def create_vehicle(db: Session, payload: VehicleCreate) -> Vehicle:
    existing = db.query(Vehicle).filter(Vehicle.plate_number == payload.plate_number).first()
    if existing:
        raise HTTPException(status_code=400, detail="Vehicle plate number already registered")


    driver = db.query(Driver).filter(Driver.id == payload.owner_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Owner not found")

    vehicle = Vehicle(**payload.model_dump())
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle

def get_vehicle(db: Session, vehicle_id: int) -> Vehicle:
    vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle
