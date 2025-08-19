from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from configuration.db import Base

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), unique=True)
    email = Column(String(100), unique=True)
    is_handicap = Column(Boolean, server_default="false", nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    vehicles = relationship("Vehicle", back_populates="owner")
    tickets = relationship("ParkingTicket", back_populates="driver")
