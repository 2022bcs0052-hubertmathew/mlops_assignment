from app import app

def test_predict():
    client = app.test_client()

    payload = {
        "customer": {
            "contract": "Month-to-Month",
            "monthly_charges_increase": True
        },
        "tickets": [
            {"days": 10, "type": "complaint"},
            {"days": 5, "type": "complaint"}
        ]
    }

    response = client.post('/predict-risk', json=payload)
    assert response.status_code == 200