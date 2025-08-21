# Parking Lot Management System

A backend service built with **FastAPI** and **SQLAlchemy** to manage parking lots, slots, drivers, vehicles, and parking transactions.  
The system provides APIs to register users with different roles, manage parking infrastructure, and handle vehicle parking operations including allocation, release, and transaction history.

---

##  Features

- **User Roles:** Admin, Police, Driver, Attendant  
- **Parking Management:**
  - Create and manage parking lots  
  - Define parking slots (standard, handicap-accessible, etc.)  
- **Driver & Vehicle Management:**
  - Register drivers  
  - Register and link vehicles to drivers  
- **Slot Allocation & Transactions:**
  - Allocate a slot when a driver parks a vehicle  
  - Store entry/exit times and calculate charges  
  - Release slot on vehicle exit  
- **Role-Based Access Control**  
- **Standardized API Response Format** for consistency  

---

##  Setup Instructions

### Prerequisites
- Python **3.10+**  
- PostgreSQL installed and running  

### Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd parking_lot_app

