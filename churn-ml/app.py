from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pickle
from features import extract_features

app = FastAPI()

# Load model
model = pickle.load(open("model.pkl", "rb"))

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

@app.post("/predict-risk")
def predict(data: InputData):
    features = extract_features(
        data.customer.dict(),
        [t.dict() for t in data.tickets]
    )

    pred = model.predict([features])[0]

    risk = "HIGH" if pred == 1 else "LOW"

    return {
        "customer_id": data.customer_id,
        "risk": risk,
        "features": {
            "freq_7": features[0],
            "freq_30": features[1],
            "freq_90": features[2],
            "avg_gap": features[3],
            "charges_increase": features[4]
        }
    }