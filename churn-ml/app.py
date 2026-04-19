from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load model
model = joblib.load("model/model.pkl")

@app.get("/")
def home():
    return {"message": "Churn Prediction API (ML Model)"}

@app.post("/predict")
def predict(data: dict):
    try:
        features = np.array([[
            data["MonthlyCharges"],
            data["tenure"],
            data["ticket_7d"],
            data["ticket_30d"],
            data["ticket_90d"],
            data["sentiment"],
            data["monthly_change"]
        ]])

        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

        return {
            "churn_prediction": int(prediction),
            "churn_probability": float(probability)
        }

    except Exception as e:
        return {"error": str(e)}