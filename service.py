from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from core import add_points, spend_points, retrieve_balance
from request_body import AddPoints, SpendPoints

app = FastAPI()

@app.post("/add")
def add(request: AddPoints):
    add_points(request.payer, request.points, request.timestamp)

@app.post("/spend")
def spend(request: SpendPoints):
    try:
        payments = spend_points(request.points)
        return payments
    except ValueError as e:
        return PlainTextResponse("Not enough points to spend!", status_code=400)
    
@app.get("/balance", status_code=200)
def balance():
    return retrieve_balance()