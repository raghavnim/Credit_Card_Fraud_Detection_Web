import joblib
import numpy as np

MODEL_PATH = "models/random_forest_model.pkl"
SCALER_PATH = "models/scaler.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


def predict_transaction(features):

    features = np.array(features).reshape(1, -1)

    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]

    probability = model.predict_proba(features_scaled)[0]

    confidence = probability[prediction] * 100

    fraud_probability = probability[1] * 100

    return prediction, confidence, fraud_probability