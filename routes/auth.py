from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from configuration.db import get_db
from schemas.auth import (
    OwnerCreate, AttendantCreate, LoginRequest,
    OwnerOut, AttendantOut
)
from services.auth import (
    register_owner_service,
    register_attendant_service,
    login_service
)
from utils.response import standard_response

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register/owner")
def register_owner(data: OwnerCreate, db: Session = Depends(get_db)):
    owner = register_owner_service(data, db)
    owner_out = OwnerOut.model_validate(owner)
    return standard_response(201, "Owner registered successfully", {"owner": owner_out.model_dump()})


@router.post("/register/attendant")
def register_attendant(data: AttendantCreate, db: Session = Depends(get_db)):
    attendant = register_attendant_service(data, db)
    attendant_out = AttendantOut.model_validate(attendant)  
    return standard_response(201, "Attendant registered successfully", {"attendant": attendant_out.model_dump()})


@router.post("/login")
def login(body: LoginRequest, db: Session = Depends(get_db)):
    token = login_service(body, db)
    return standard_response(200, "Login successful", token)
