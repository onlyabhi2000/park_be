from pydantic import BaseModel
from typing import Optional, List, Any
from datetime import datetime



# Request Schemas


class TicketCreate(BaseModel):
    driver_id: int
    vehicle_id: int
    lot_id: int
    attendant_id: Optional[int] = None

    class Config:
        orm_mode = True


class TicketClose(BaseModel):
    mark_paid: bool = False

    class Config:
        orm_mode = True


# Core Ticket Response


class TicketOut(BaseModel):
    id: int
    ticket_number: str

    vehicle_id: int
    driver_id: int
    lot_id: int
    slot_id: Optional[int] = None

    entry_time: Optional[datetime] = None
    exit_time: Optional[datetime] = None

    parking_fee: Optional[float] = None
    payment_status: str
    is_active: bool

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True



# Standard Response Wrappers


class APIResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[Any] = None


class TicketResponse(APIResponse):
    data: Optional[TicketOut]


class TicketListResponse(APIResponse):
    data: List[TicketOut] = []
