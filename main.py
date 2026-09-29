from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MLOps Production API")

class PredictionInput(BaseModel):
    feature1: float
    feature2: float

@app.get("/")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}

@app.post("/predict")
def predict(data: PredictionInput):
    # Simulated model inference logic
    score = (data.feature1 * 0.4) + (data.feature2 * 0.6)
    prediction = 1 if score > 2.5 else 0
    return {
        "status": "success",
        "prediction": prediction,
        "confidence": round(score, 2)
    }
