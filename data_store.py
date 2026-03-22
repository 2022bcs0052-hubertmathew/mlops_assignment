# Simulated database

customers = {}
tickets_db = {}

def save_customer(customer_id, customer_data):
    customers[customer_id] = customer_data

def save_tickets(customer_id, tickets):
    tickets_db[customer_id] = tickets

def get_customer(customer_id):
    return customers.get(customer_id, {})

def get_tickets(customer_id):
    return tickets_db.get(customer_id, [])