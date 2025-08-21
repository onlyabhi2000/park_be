from pydantic import BaseModel

class ParkingLotCreate(BaseModel):
    name: str
    address: str | None = None
    total_capacity: int
    available_slots: int

class ParkingLotOut(BaseModel):
    id: int
    name: str
    address: str | None = None
    total_capacity: int
    available_slots: int
    owner_id: int

    class Config:
        from_attributes = True  
