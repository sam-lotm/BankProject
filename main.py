from fastapi import FastAPI
from accounts.router import router as accounts_router

app = FastAPI(title="Bank App")

app.include_router(accounts_router, prefix="/accounts", tags=["accounts"])

@app.get("/")
def root():
    return {"message": "Bank API is running"}