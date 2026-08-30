from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

MODEL_PATH = "/app/fraud_model.pkl"

model = joblib.load(MODEL_PATH)


class PredictionRequest(BaseModel):
    instances: list


@app.get("/")
def root():
    return {
        "status": "ready",
        "model": "fraud-model"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/v1/models/fraud-model:predict")
def predict(request: PredictionRequest):

    X = np.asarray(request.instances)

    predictions = model.predict(X)

    response = {
        "predictions": predictions.tolist()
    }

    if hasattr(model, "predict_proba"):
        response["probabilities"] = model.predict_proba(X).tolist()

    return response
