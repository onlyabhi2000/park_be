from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.configuration.db import get_db
from app.dependencies.role_deps import owner_required
from app.services.lots import create_lot_service
from app.schemas.lots import ParkingLotCreate, ParkingLotOut
from app.utils.response import standard_response

router = APIRouter(prefix="/lots", tags=["Parking Lots"])


@router.post("/")
def create_lot(payload: ParkingLotCreate, owner=Depends(owner_required), db: Session = Depends(get_db)):
    lot = create_lot_service(payload, owner, db)
    lot_out = ParkingLotOut.model_validate(lot)   
    return standard_response(201, "Parking lot created successfully", {"lot": lot_out.model_dump()})
