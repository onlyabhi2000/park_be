from pydantic import BaseModel
from typing import Optional

class DriverCreate(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None
    is_handicap: bool = False

class DriverOut(BaseModel):
    id: int
    name: str
    phone: str
    email: Optional[str] = None
    is_handicap: bool

    class Config:
        from_attributes = True
