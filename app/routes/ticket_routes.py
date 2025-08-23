from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from decimal import Decimal

from app.configuration.db import get_db
from app.services import ticket_service
from app.utils.response import standard_response  # (status_code, message, data)

router = APIRouter(prefix="/tickets", tags=["Parking Tickets"])
from app.schemas.ticket import TicketListResponse , TicketClose , TicketCreate , TicketResponse

# --- helpers ---

def _ticket_to_dict(t) -> dict:
    """Serialize ParkingTicket ORM to JSON-safe dict."""
    return {
        "id": t.id,
        "ticket_number": t.ticket_number,
        "vehicle_id": t.vehicle_id,
        "driver_id": t.driver_id,
        "lot_id": t.lot_id,
        "slot_id": t.slot_id,
        "entry_time": t.entry_time.isoformat() if t.entry_time else None,
        "exit_time": t.exit_time.isoformat() if t.exit_time else None,
        "parking_fee": float(t.parking_fee) if isinstance(t.parking_fee, Decimal) else t.parking_fee,
        "payment_status": t.payment_status,
        "is_active": bool(t.is_active),
        "created_at": t.created_at.isoformat() if t.created_at else None,
        "updated_at": t.updated_at.isoformat() if t.updated_at else None,
    }


@router.post("/", response_model=TicketResponse)
def allocate_ticket(payload: TicketCreate, db: Session = Depends(get_db)):
    ticket = ticket_service.allocate_ticket(db, payload)
    return standard_response(
        status_code=201,
        message="Ticket allocated successfully",
        data=ticket
    )



@router.post("/{ticket_id}/close", response_model=TicketResponse)
def close_ticket(ticket_id: int, payload: TicketClose, db: Session = Depends(get_db)):
    ticket = ticket_service.close_ticket(db, ticket_id, payload.mark_paid)
    return standard_response(
        status_code=200,
        message="Ticket closed successfully",
        data=ticket
    )


@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = ticket_service.get_ticket(db, ticket_id)
    return standard_response(
        status_code=200,
        message="Ticket retrieved successfully",
        data=ticket
    )