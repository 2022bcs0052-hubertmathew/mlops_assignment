from flask import Flask, request, jsonify
from rules import predict_risk

app = Flask(__name__)

@app.route('/predict-risk', methods=['POST'])
def predict():
    data = request.json
    customer = data['customer']
    tickets = data['tickets']

    risk = predict_risk(customer, tickets)

    return jsonify({"risk": risk})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)