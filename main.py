from fastapi import FastAPI

app = FastAPI(title="MLOps Prediction Service", version="1.0.0")

@app.get("/")
def read_root():
    return {"status": "online", "message": "MLOps API is active!"}

@app.post("/predict")
def predict(data: dict):
    return {"status": "success", "input_data": data, "prediction": 42.0}
