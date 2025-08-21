from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime, func
from app.configuration.db import Base

class LotNotification(Base):
    __tablename__ = "lot_notifications"

    id = Column(Integer, primary_key=True, index=True)
    lot_id = Column(Integer, ForeignKey("parking_lots.id", ondelete="CASCADE"), nullable=False)
    notification_type = Column(String(30), nullable=False)  # FULL, AVAILABLE, CAPACITY_WARNING
    message = Column(Text, nullable=False)
    is_sent = Column(Boolean, server_default="false", nullable=False)
    recipient_type = Column(String(20), nullable=False)  # SECURITY, OWNER, ATTENDANT

    created_at = Column(DateTime(timezone=True), server_default=func.now())
