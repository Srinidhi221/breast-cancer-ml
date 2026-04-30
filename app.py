from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("saved_models/logistic_regression.pkl")
scaler = joblib.load("saved_models/scaler.pkl")

@app.route('/')
def home():
    return "API is running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['features']
    data = np.array(data).reshape(1, -1)
    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)[0]

    return jsonify({
        "prediction": int(prediction),
        "result": "Malignant" if prediction == 1 else "Benign"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)