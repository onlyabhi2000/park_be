from fastapi import FastAPI
from routes import auth
import models
from configuration.db import Base
from routes import lots
from routes import vehicle , drivers , parking_slot


app = FastAPI()
app.include_router(auth.router)
app.include_router(lots.router)
app.include_router(vehicle.router)
app.include_router(drivers.router)
app.include_router(parking_slot.router)



@app.get("/")
def read_root():
    return {"message": "Welcome to parking system"}
