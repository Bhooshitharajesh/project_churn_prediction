import pandas as pd
import joblib

from utils import add_age_group

model=joblib.load("model/churn_pipeline.pkl")

def predict_churn(df:dict):
    df=pd.DataFrame([df])

    prediction=model.predict(df)[0]
    return "yes"if prediction==1 else "no"

