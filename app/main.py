from fastapi import FastAPI
from app.configuration.db import Base  
from app.utils.router_helper import include_all_routers 

app = FastAPI()

include_all_routers(app)

@app.get("/")
def read_root():
    return {"message": "Welcome to parking system"}