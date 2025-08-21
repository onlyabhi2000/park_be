# Ensure every model file is imported once so SQLAlchemy sees them all
from .owner import Owner
from .parking_lot import ParkingLot
from .attendant import Attendant
from .driver import Driver
from .vehicle import Vehicle
from .parking_slot import ParkingSlot
from .parking_ticket import ParkingTicket
from .lot_notification import LotNotification
