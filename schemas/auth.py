from pydantic import BaseModel , EmailStr

class OwnerCreate(BaseModel):
    name : str
    email : EmailStr
    password : str


class OwnerOut(BaseModel):
    id : int
    name : str
    email : EmailStr
    is_active: bool
    class Config: from_attributes = True

class AttendantCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str | None = None
    is_active: bool = True


class AttendantOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str | None = None
    employee_id: str
    is_active: bool
    class Config: from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str