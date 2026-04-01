from fastapi import FastAPI
from app.schema import CoustmerData
from app.model_loader import predict_churn

app=FastAPI(title="Churn Prediction API")

@app.get("/")
def home():
    return {"status":"API is running"}

@app.post("/predict")
def predict(df:CoustmerData):
    result=predict_churn(df.dict())
    return {"churn_prediction:",result}






