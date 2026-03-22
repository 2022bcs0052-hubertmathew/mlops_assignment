from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict():
    payload = {
        "customer_id": "C1",
        "customer": {
            "contract": "Month-to-Month",
            "monthly_charges_increase": True
        },
        "tickets": [
            {"days": 5, "type": "complaint"},
            {"days": 2, "type": "complaint"}
        ]
    }

    response = client.post("/predict-risk", json=payload)
    assert response.status_code == 200
    assert "risk" in response.json()