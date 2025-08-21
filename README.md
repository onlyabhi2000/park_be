```Parking Lot Management System```

A backend service built with FastAPI and SQLAlchemy to manage parking lots, slots, drivers, vehicles, and parking transactions. The system provides APIs to register users with different roles, manage parking infrastructure, and handle vehicle parking operations including allocation, release, and transaction history.

```Features```

User Roles: Admin, Police, Driver , Attendant


```Parking Management:```

Create and manage parking lots

Define parking slots under each lot (standard, handicap-accessible, etc.)

Driver & Vehicle Management:

Register drivers

Register and link vehicles to drivers

Slot Allocation & Transactions:

Allocate a slot when a driver parks a vehicle

Store entry/exit times and calculate charges

Release slot on vehicle exit

Role-based Access Control

Standard API Response Format for consistency




```Setup Instructions```
Prerequisites

Python 3.10+

PostgreSQL installed and running

Installation

Clone the repository

git clone <repo-url>
cd parking_lot_app


```Create and activate virtual environment```

python3 -m venv env
source env/bin/activate


Install dependencies

pip install -r requirements.txt


Configure database URL in app/core/config.py

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/parking_lot"


```Run migrations ```

alembic upgrade head


Start the server

uvicorn main:app --reload


```API Endpoints```

Auth: /auth/register, /auth/login

Parking Lots: /lots/

Parking Slots: /slots/

Drivers: /drivers/

Vehicles: /vehicles/

Transactions: /transactions/

