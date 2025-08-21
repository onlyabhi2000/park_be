from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies.role_deps import owner_required
from configuration.db import get_db
from services.lots import create_lot_service
from schemas.lots import ParkingLotCreate, ParkingLotOut
from utils.response import standard_response

router = APIRouter(prefix="/lots", tags=["Parking Lots"])


@router.post("/")
def create_lot(payload: ParkingLotCreate, owner=Depends(owner_required), db: Session = Depends(get_db)):
    lot = create_lot_service(payload, owner, db)
    lot_out = ParkingLotOut.model_validate(lot)   
    return standard_response(201, "Parking lot created successfully", {"lot": lot_out.model_dump()})
