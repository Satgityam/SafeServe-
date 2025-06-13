import pandas as pd
from engine.feature_extractor import extract_features
from engine.fraud_detector import detect_fraud
from alerts.alert_logger import log_alerts
import os

# Path to CSV
DATA_PATH = "data/transactions.csv"

def main():
    if not os.path.exists(DATA_PATH):
        print("❌ transactions.csv not found. Run the simulator first.")
        return

    df = pd.read_csv(DATA_PATH)

    # Run feature extraction
    df = extract_features(df)

    # Run fraud detection
    df = detect_fraud(df)

    # Log alerts for frauds
    frauds = df[df['is_fraud'] == True]
    log_alerts(frauds)

    # Save back to CSV
    df.to_csv(DATA_PATH, index=False)
    print(f"✅ Processed {len(df)} transactions and saved with fraud labels.")

if __name__ == "__main__":
    main()
