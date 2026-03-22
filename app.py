from flask import Flask, request, jsonify
from rules import predict_risk
from data_store import save_customer, save_tickets, get_customer, get_tickets

app = Flask(__name__)

# 🔹 1. Ingest Customer Data
@app.route('/ingest/customer', methods=['POST'])
def ingest_customer():
    data = request.json
    customer_id = data['customer_id']
    customer_data = data['customer']

    save_customer(customer_id, customer_data)

    return jsonify({"message": "Customer stored"})

# 🔹 2. Ingest Ticket Data
@app.route('/ingest/tickets', methods=['POST'])
def ingest_tickets():
    data = request.json
    customer_id = data['customer_id']
    tickets = data['tickets']

    save_tickets(customer_id, tickets)

    return jsonify({"message": "Tickets stored"})

# 🔹 3. Predict Risk
@app.route('/predict-risk/<customer_id>', methods=['GET'])
def predict(customer_id):
    customer = get_customer(customer_id)
    tickets = get_tickets(customer_id)

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    risk = predict_risk(customer, tickets)

    return jsonify({
        "customer_id": customer_id,
        "risk": risk
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)