from fastapi import APIRouter
from database import fake_db

router = APIRouter()

@router.post("/create")
def create_account(owner_name: str, balance: float = 0.0):
    account_id = len(fake_db["accounts"]) + 1
    fake_db["accounts"][account_id] = {
        "id": account_id,
        "owner_name": owner_name,
        "balance": balance
    }
    return fake_db["accounts"][account_id]

@router.get("/{account_id}")
def get_account(account_id: int):
    account = fake_db["accounts"].get(account_id)
    if not account:
        return {"error": "Account not found"}
    return account