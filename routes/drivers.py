from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from configuration.db import get_db
from schemas.driver import DriverCreate , DriverOut
from services.driver import create_driver ,get_driver
from utils.response import standard_response

router = APIRouter(prefix = "/drivers" , tags = ["Drivers"])
@router.post("/")
def register_driver(payload: DriverCreate, db: Session = Depends(get_db)):
    driver = create_driver(db, payload)
    data = DriverOut.model_validate(driver).model_dump()
    return standard_response(201, "Driver registered successfully", data)


@router.get("/{driver_id}")
def fetch_driver(driver_id : int , db : Session = Depends(get_db)):
    driver = get_driver(db , driver_id)
    data = DriverOut.model_validate(driver).model_dump()
    return standard_response(200 , "Driver fetch successfully" , data)
