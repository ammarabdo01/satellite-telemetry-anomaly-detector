import pandas as pd
from sklearn.ensemble import IsolationForest


def train_and_detect(file_path="telemetry_data.csv"):
    df = pd.read_csv(file_path)
    features = ['temperature', 'voltage', 'current']

    # Isolation Forest Model
    model = IsolationForest(contamination=0.05, random_state=42)
    df['anomaly'] = model.fit_predict(df[features])

    # تحويل النتيجة (-1 تعني Anomaly, 1 تعني Normal)
    df['is_anomaly'] = df['anomaly'].apply(lambda x: True if x == -1 else False)

    return df


if __name__ == "__main__":
    results = train_and_detect()
    anomalies_found = results[results['is_anomaly'] == True]
    print(f"Total Anomalies Detected: {len(anomalies_found)}")
    print(anomalies_found[['timestamp', 'temperature', 'voltage', 'current']].head())
    if __name__ == "__main__":
        results = train_and_detect()
        anomalies = results[results['is_anomaly'] == True]

        print("--- Anomalies Detected ---")
        print(anomalies[['timestamp', 'temperature', 'voltage', 'current']].head(10))