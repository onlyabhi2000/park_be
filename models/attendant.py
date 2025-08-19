from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from configuration.db import Base

class Attendant(Base):
    __tablename__ = "attendants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), unique=True)
    employee_id = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(200), nullable=False)  # hashed
    is_active = Column(Boolean, server_default="true", nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    tickets = relationship("ParkingTicket", back_populates="attendant")
