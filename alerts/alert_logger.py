def log_alerts(frauds):
    with open("alerts/log.txt", "w") as f:
        for _, row in frauds.iterrows():
            f.write(f"[ALERT] Fraud detected: {row['transaction_id']} - {row['amount']}\n")
