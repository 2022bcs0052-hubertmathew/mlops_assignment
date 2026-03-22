def extract_features(customer, tickets):
    freq_7 = len([t for t in tickets if t["days"] <= 7])
    freq_30 = len([t for t in tickets if t["days"] <= 30])
    freq_90 = len([t for t in tickets if t["days"] <= 90])

    avg_gap = sum([t["days"] for t in tickets]) / len(tickets) if tickets else 0

    return [
        freq_7,
        freq_30,
        freq_90,
        avg_gap,
        int(customer["monthly_charges_increase"])
    ]