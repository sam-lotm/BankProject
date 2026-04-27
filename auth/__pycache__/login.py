from fastapi import APIRouter, HTTPException
from database import fake_db
from pydantic import EmailStr
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["sha256_crypt"])


router = APIRouter()


@router.get("/login")
def login(email: EmailStr, password: str):

    user = fake_db["users"].get(email)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect Login")

    # check password against stored hash
    if not pwd_context.verify(password, user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect Login")
    else:
        return {"message": "You Are Logged in"}
    
