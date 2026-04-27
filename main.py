from fastapi import FastAPI
from accounts.router import router as accounts_router
from transactions.router import router as transactions_router
from auth.router import router as auth_router
app = FastAPI(title="Bank App")

app.include_router(accounts_router, prefix="/accounts", tags=["accounts"])

app.include_router(transactions_router, prefix="/transactions", tags=["transactions"])

app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "Bank API is running"}