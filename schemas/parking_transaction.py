from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ParkingTransactionBase(BaseModel):
    driver_id: int
    vehicle_id: int
    slot_id: int
    lot_id: int

class ParkingTransactionCreate(ParkingTransactionBase):
    pass