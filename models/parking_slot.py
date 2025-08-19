from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from configuration.db import Base

class ParkingSlot(Base):
    __tablename__ = "parking_slots"

    id = Column(Integer, primary_key=True, index=True)
    slot_number = Column(String(10), nullable=False)
    lot_id = Column(Integer, ForeignKey("parking_lots.id", ondelete="CASCADE"), nullable=False)
    row_identifier = Column(String(5), nullable=False)
    is_occupied = Column(Boolean, server_default="false", nullable=False)
    is_handicap_accessible = Column(Boolean, server_default="false", nullable=False)
    distance_from_exit = Column(Integer)
    slot_size = Column(String(20), server_default="standard")  # standard, large, compact

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    lot = relationship("ParkingLot", back_populates="slots")
    tickets = relationship("ParkingTicket", back_populates="slot")
