import pandas as pd
from sklearn.ensemble import IsolationForest

model = IsolationForest(n_estimators=100, contamination=0.05)

def detect_anomaly(entry, packets_data, anomalies):
    if len(packets_data) < 20:
        return
    df = pd.DataFrame(packets_data[-100:])
    features = df[['len']]
    model.fit(features)
    prediction = model.predict([[entry['len']]])
    if prediction[0] == -1:
        anomalies.append(entry)
