from fastapi import APIRouter, HTTPException
from database import fake_db
from pydantic import EmailStr
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"])
router = APIRouter()

@router.post("/register")
def register(email: EmailStr, password: str):
    if email in fake_db["users"]:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = pwd_context.hash(password)
    
    fake_db["users"][email] = {
        "email": email,
        "password": hashed_password
    }
    
    return {"message": "You Are Registered"}