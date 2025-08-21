from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from datetime import datetime
from decimal import Decimal
import uuid

from app.models.parking_ticket import ParkingTicket
from app.models.parking_slot import ParkingSlot
from app.models.vehicle import Vehicle
from app.models.driver import Driver


def generate_ticket_number() -> str:
    return f"TKT-{uuid.uuid4().hex[:8].upper()}"