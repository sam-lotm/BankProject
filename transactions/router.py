from fastapi import APIRouter
from database import fake_db

router = APIRouter()

@router.post("/deposit")
def deposit(account_id: int, amount: float, description: str):
    account = fake_db["accounts"].get(account_id)
    if not account:
        return {"error": "Account not found"}
    
    balance = account["balance"]
    new_balance = balance + amount

    fake_db["accounts"][account_id]["balance"] = new_balance

    fake_db["transactions"].append({
        "account_id": account_id,
        "type": "deposit",
        "amount": amount,
        "balance_after": new_balance,
        "description": description
    })
    return {"account_id": account_id, "new_balance": new_balance}

@router.post("/withdrawal")
def withdrawal(account_id: int, amount: float, description: str):
    account = fake_db["accounts"].get(account_id)
    if not account:
        return{"error": "Account not found"}

    balance = account["balance"]
    new_balance = balance - amount
    if amount > balance:
        return{"error": "Insufficient Funds"}
    
    balance = new_balance

    fake_db["accounts"][account_id]["balance"] = new_balance
    fake_db["transactions"].append({
        "account_id": account_id,
        "type": "waithdrawl",
        "amount": amount,
        "balance_after": new_balance,
        "description": description
    })
    return {"account_id": account_id, "new_balance": new_balance}

@router.get("/history")
def get_history(account_id: int):
    account = fake_db["accounts"].get(account_id)
    if not account:
        return{"error": "Account not found"}

    history = [t for t in fake_db["transactions"] if t["account_id"] == account_id]
    return {"account_id": account_id, "transactions": history}