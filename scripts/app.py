import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load trained model and vectorizer (make sure the path is correct)
model = joblib.load('../models/model.joblib')
vectorizer = joblib.load('../models/vectorizer.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = vectorizer.transform([data['text']])
    prediction = model.predict(text)
    probability = model.predict_proba(text)
    return jsonify({'prediction': int(prediction[0]), 'probability': probability[0].tolist()})

if __name__ == '__main__':
    app.run(debug=True)

