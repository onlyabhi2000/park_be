from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ParkingSlotBase(BaseModel):
    slot_number: str
    row_identifier: str
    is_handicap_accessible: Optional[bool] = False
    distance_from_exit: Optional[int] = None
    slot_size: Optional[str] = "standard"  # standard, large, compact



class ParkingSlotCreate(ParkingSlotBase):
    lot_id: int


class ParkingSlotUpdate(BaseModel):
    is_occupied: Optional[bool] = None
    is_handicap_accessible: Optional[bool] = None
    distance_from_exit: Optional[int] = None
    slot_size: Optional[str] = None


class ParkingSlotOut(BaseModel):
    id: int
    slot_number: str
    lot_id: int
    row_identifier: str
    is_handicap_accessible: bool
    distance_from_exit: int
    slot_size: str
    is_occupied: bool

    model_config = {
        "from_attributes": True
    }