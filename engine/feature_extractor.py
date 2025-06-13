def extract_features(df):
    df["high_value"] = df["amount"] > 4000
    df["odd_hour"] = df["timestamp"].str.contains(" 00:| 01:| 02:| 03:")
    df["device_changed"] = df["device_id"].duplicated(keep=False) == False
    return df
