from pydantic import BaseModel

class VehicleCreate(BaseModel):
    plate_number: str
    make: str
    model: str | None = None
    color: str
    vehicle_type: str
    owner_id: int

class VehicleOut(BaseModel):
    id: int
    plate_number: str
    make: str
    model: str | None = None
    color: str
    vehicle_type: str
    owner_id: int | None = None

    class Config:
        from_attributes = True
