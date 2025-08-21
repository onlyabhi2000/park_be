from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Numeric, func
from sqlalchemy.orm import relationship
from app.configuration.db import Base

class ParkingTicket(Base):
    __tablename__ = "parking_tickets"

    id = Column(Integer, primary_key=True, index=True)
    ticket_number = Column(String(20), unique=True, nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id", ondelete="SET NULL"), nullable=False)
    driver_id = Column(Integer, ForeignKey("drivers.id", ondelete="SET NULL"), nullable=False)
    lot_id = Column(Integer, ForeignKey("parking_lots.id", ondelete="CASCADE"), nullable=False)
    slot_id = Column(Integer, ForeignKey("parking_slots.id", ondelete="SET NULL"), nullable=False)
    attendant_id = Column(Integer, ForeignKey("attendants.id", ondelete="SET NULL"))

    entry_time = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    exit_time = Column(DateTime(timezone=True), nullable=True)
    parking_fee = Column(Numeric(10, 2))
    payment_status = Column(String(20), server_default="pending")  # pending, paid, failed
    is_active = Column(Boolean, server_default="true", nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    vehicle = relationship("Vehicle", back_populates="tickets")
    driver = relationship("Driver", back_populates="tickets")
    lot = relationship("ParkingLot", back_populates="tickets")
    slot = relationship("ParkingSlot", back_populates="tickets")
    attendant = relationship("Attendant", back_populates="tickets")
