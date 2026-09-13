import pandas as pd
import matplotlib.pyplot as plt
from model import train_and_detect

df = train_and_detect()

plt.figure(figsize=(12, 6))
# رسم القراءات العادية
plt.plot(df['timestamp'], df['temperature'], label='Temperature', color='blue', alpha=0.6)

# تحديد ورسم الأخطاء باللون الأحمر
anomalies = df[df['is_anomaly'] == True]
plt.scatter(anomalies['timestamp'], anomalies['temperature'], color='red', label='Anomaly Detected', zorder=5)

plt.title('Satellite Telemetry - Anomaly Detection')
plt.xlabel('Timestamp')
plt.ylabel('Temperature')
plt.legend()
plt.tight_layout()
plt.show()