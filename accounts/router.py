from fastapi import APIRouter
from database import fake_db
from datetime import date
from pydantic import EmailStr
router = APIRouter()

@router.post("/create")
def create_account(owner_name: str, DOB: date, Ph_no: str, email: EmailStr, balance: float = 0.0):
    age = (date.today() - DOB).days //365
    if age< 18:
       return {"error": "Must be 18 or older to open an account"}
    for account in fake_db["accounts"].values():
        if account["Phone_Number"] == Ph_no:
            return {"error": "Number already registered"}
        if account["Email"] == email:
            return {"error": "Email already registered"}

    account_id = len(fake_db["accounts"]) + 1
    fake_db["accounts"][account_id] = {
        "id": account_id,
        "owner_name": owner_name,
        "balance": balance,
        "DateofBirth": DOB,
        "Phone_Number": Ph_no,
        "Email": email
    }
    return fake_db["accounts"][account_id]

@router.get("/{account_id}")
def get_account(account_id: int):
    account = fake_db["accounts"].get(account_id)
    if not account:
        return {"error": "Account not found"}
    return account