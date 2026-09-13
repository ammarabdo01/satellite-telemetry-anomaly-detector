import pandas as pd
import numpy as np


def generate_telemetry_data(n_samples=1000):
    np.random.seed(42)
    timestamps = pd.date_range(start="2026-01-01", periods=n_samples, freq="1min")

    # القراءات الطبيعية
    temp = np.random.normal(loc=25, scale=2, size=n_samples)  # 25°C average
    voltage = np.random.normal(loc=12, scale=0.5, size=n_samples)  # 12V average
    current = np.random.normal(loc=5, scale=0.2, size=n_samples)  # 5A average

    df = pd.DataFrame({'timestamp': timestamps, 'temperature': temp, 'voltage': voltage, 'current': current})

    # إدخال شذوذ/أعطال مصنعة (Anomalies) بنسبة 5%
    anomaly_indices = np.random.choice(n_samples, size=int(n_samples * 0.05), replace=False)
    for idx in anomaly_indices:
        df.loc[idx, 'temperature'] += np.random.choice([30, -30])  # قفزة مفاجئة للحرارة
        df.loc[idx, 'voltage'] += np.random.choice([10, -8])  # هبوط أو ارتفاع حاد للفولت

    return df


if __name__ == "__main__":
    df = generate_telemetry_data()
    df.to_csv("telemetry_data.csv", index=False)
    print("Data generated successfully and saved to telemetry_data.csv")