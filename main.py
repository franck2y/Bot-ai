from fastapi import FastAPI
from trading import execute_trade, get_account_info
from pydantic import BaseModel

app = FastAPI()

class TradeRequest(BaseModel):
    asset: str
    direction: str
    amount: float

@app.get("/status")
def status():
    return get_account_info()

@app.post("/trade")
def trade(req: TradeRequest):
    return execute_trade(req.asset, req.direction, req.amount)
