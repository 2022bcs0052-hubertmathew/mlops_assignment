def predict_risk(customer, tickets):
    ticket_count_30 = len([t for t in tickets if t['days'] <= 30])

    if ticket_count_30 > 5:
        return "HIGH"

    if customer['monthly_charges_increase'] and ticket_count_30 >= 3:
        return "MEDIUM"

    if customer['contract'] == "Month-to-Month":
        for t in tickets:
            if t['type'] == "complaint":
                return "HIGH"

    return "LOW"