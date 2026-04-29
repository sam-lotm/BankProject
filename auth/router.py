from fastapi import APIRouter, HTTPException
from database import fake_db
from pydantic import EmailStr
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["sha256_crypt"])
SECRET_KEY = "your-secret-key-change-this"
ALGORITHM = "HS256"
router = APIRouter()

def create_token(email: str):
    expire = datetime.utcnow() + timedelta(minutes=30)
    data = {
        "sub": email,
        "exp": expire
    }
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

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

@router.post("/login")
def login(email: EmailStr, password: str):
    user = fake_db["users"].get(email)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect Login")
    if not pwd_context.verify(password, user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect Login")
    token = create_token(email)
    return {"access_token": token, "token_type": "bearer"}