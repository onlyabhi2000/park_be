from fastapi import FastAPI
from routes import auth
import models
from configuration.db import Base
from routes import lots


app = FastAPI()
app.include_router(auth.router)
app.include_router(lots.router)



@app.get("/")
def read_root():
    return {"message": "Welcome to parking system"}
