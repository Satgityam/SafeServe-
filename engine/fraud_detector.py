def detect_fraud(df):
    df["is_fraud"] = df["high_value"] | df["odd_hour"] | df["device_changed"]
    return df
