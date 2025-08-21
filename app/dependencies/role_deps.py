from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.configuration.db import get_db
from app.core.security import decode_token
from app.models.owner import Owner
from app.models.attendant import Attendant

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

bearer_scheme = HTTPBearer()

def get_current_identity(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), db: Session = Depends(get_db)):
    token = credentials.credentials  
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    uid = payload.get("user_id")
    role = payload.get("role")
    obj = None
    if role == "OWNER":
        obj = db.query(Owner).get(uid)
    elif role == "ATTENDANT":
        obj = db.query(Attendant).get(uid)
    if not obj:
        raise HTTPException(status_code=401, detail="Invalid authentication")
    return {"role": role, "obj": obj}


def owner_required(identity=Depends(get_current_identity)):
    if identity["role"] != "OWNER":
        raise HTTPException(status_code=403, detail="Owner access required")
    return identity["obj"]

def attendant_required(identity=Depends(get_current_identity)):
    if identity["role"] != "ATTENDANT":
        raise HTTPException(status_code=403, detail="Attendant access required")
    return identity["obj"]
