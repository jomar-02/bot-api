from flask import Flask, request, jsonify
from flask_cors import CORS
from data_preprocessing import get_response
from train import train_model

app = Flask(__name__)
CORS(app)

@app.get("/")
def index_get():
    return jsonify({"message": "Test API"})
   
@app.post("/predict")   
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer" : response}
    return jsonify(message)

if __name__ == "__main__":
    train_model()
    app.run()
