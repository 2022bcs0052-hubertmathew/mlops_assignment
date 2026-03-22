from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data storage
customers = {}
tickets_db = {}

# Models
class Ticket(BaseModel):
    days: int
    type: str

class Customer(BaseModel):
    contract: str
    monthly_charges_increase: bool

class InputData(BaseModel):
    customer_id: str
    customer: Customer
    tickets: List[Ticket]

# Rule logic
def predict_risk(customer, tickets):
    ticket_count_30 = len([t for t in tickets if t.days <= 30])

    if ticket_count_30 > 5:
        return "HIGH"

    if customer.monthly_charges_increase and ticket_count_30 >= 3:
        return "MEDIUM"

    if customer.contract == "Month-to-Month":
        for t in tickets:
            if t.type == "complaint":
                return "HIGH"

    return "LOW"

# API
@app.post("/predict-risk")
def predict(data: InputData):
    risk = predict_risk(data.customer, data.tickets)
    return {"customer_id": data.customer_id, "risk": risk}

@app.get("/")
def home():
    return {"message": "API running"}