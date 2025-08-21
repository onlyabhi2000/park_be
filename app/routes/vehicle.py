from fastapi import APIRouter  , Depends
from app.services.vehicles import create_vehicle , get_vehicle
from sqlalchemy.orm import Session
from app.configuration.db import get_db
from app.models.vehicle import Vehicle
from app.schemas.vehicles import VehicleCreate , VehicleOut
from app.utils.response import standard_response

router = APIRouter(prefix = '/vehicles' , tags = ['Vehicles'])


@router.post('/')
def register_vehicle(payload:VehicleCreate , db : Session = Depends(get_db)):
    vehicle = create_vehicle( db , payload)
    data = VehicleOut.model_validate(vehicle).model_dump()
    return standard_response(201 , "Vehicle registered sucessfuly" , data)

@router.get('/{vehicle_id}')
def fetch_vehicle(vehicle_id : int , db : Session = Depends(get_db)):
    vehicle = get_vehicle(db , vehicle_id)
    data = VehicleOut.model_validate(vehicle).model_dump()
    return standard_response(200 , "Vehicle fetched successfully" , data)