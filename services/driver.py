from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.driver import Driver
from schemas.driver import DriverCreate

def create_driver(db: Session, payload: DriverCreate) -> Driver:
    existing = db.query(Driver).filter(Driver.phone == payload.phone).first()
    if existing:
        raise HTTPException(status_code=400, detail="Phone already registered")

    driver = Driver(**payload.model_dump())
    db.add(driver)
    db.commit()
    db.refresh(driver)
    return driver

def get_driver(db: Session, driver_id: int) -> Driver:
    driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver
