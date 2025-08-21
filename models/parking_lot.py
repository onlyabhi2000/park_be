from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from configuration.db import Base

class ParkingLot(Base):
    __tablename__ = "parking_lots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(Text)
    total_capacity = Column(Integer, nullable=False)
    available_slots = Column(Integer, nullable=False)
    is_full = Column(Boolean, server_default="false", nullable=False)
    owner_name = Column(String(100), server_default="Sanjay") 

    owner_id = Column(Integer, ForeignKey("owners.id", ondelete="SET NULL"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    owner = relationship("Owner", back_populates="lots")
    slots = relationship("ParkingSlot", back_populates="lot", cascade="all,delete-orphan")
    tickets = relationship("ParkingTicket", back_populates="lot")
