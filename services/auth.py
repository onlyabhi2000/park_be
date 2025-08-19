import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from core.security import hash_password, verify_password, create_access_token
from models.owner import Owner
from models.attendant import Attendant
from schemas.auth import OwnerCreate, AttendantCreate, LoginRequest


def register_owner_service(data: OwnerCreate, db: Session):
    if db.query(Owner).filter(Owner.email == data.email).first():
        raise HTTPException(status_code=400, detail="Owner email already registered")

    owner = Owner(
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        is_active=True
    )
    db.add(owner)
    db.commit()
    db.refresh(owner)
    return owner


def register_attendant_service(data: AttendantCreate, db: Session):
    if db.query(Attendant).filter(Attendant.email == data.email).first():
        raise HTTPException(status_code=400, detail="Attendant email already registered")

    new_employee_id = f"EMP{str(uuid.uuid4().int)[:6]}"  

    attendant = Attendant(
        name=data.name,
        email=data.email,
        phone=data.phone,
        is_active=data.is_active,
        employee_id=new_employee_id,
        password=hash_password(data.password)
    )
    db.add(attendant)
    db.commit()
    db.refresh(attendant)
    return attendant


def login_service(body: LoginRequest, db: Session):
    user = db.query(Owner).filter(Owner.email == body.email).first()
    role = "OWNER"
    if not user:
        user = db.query(Attendant).filter(Attendant.email == body.email).first()
        role = "ATTENDANT"

    if not user or not verify_password(body.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token({"user_id": user.id, "role": role})
    return {"access_token": token, "token_type": "bearer"}
