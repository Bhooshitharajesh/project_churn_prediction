from pydantic import BaseModel

class CoustmerData(BaseModel):
    CreditScore:float
    Age:int
    Tenure:int
    Balance:float
    NumOfProducts:int
    EstimatedSalary:float
    Geography:str
    Gender:str
    HasCrCard:int
    IsActiveMember:int
    