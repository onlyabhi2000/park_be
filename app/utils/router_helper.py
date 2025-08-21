from fastapi import FastAPI
from app.routes import auth, lots, vehicle, drivers, parking_slot

def include_all_routers(app: FastAPI):
    """
    Function to include all API routers.
    Add new routers to the list below as you create them.
    """
    routers = [
        auth.router,
        lots.router,
        vehicle.router,
        drivers.router,
        parking_slot.router
    ]
    
    for router in routers:
        app.include_router(router)