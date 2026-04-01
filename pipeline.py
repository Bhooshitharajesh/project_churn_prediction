from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

df=pd.read_csv(r"C:\Users\BHOOSHITHA\OneDrive\Desktop\course\project\app\data\Churn_Modelling.csv")
df=df.drop(['RowNumber','CustomerId','Surname'],axis=1)
x=df.drop('Exited',axis=1)
y=df['Exited']
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,stratify=y)

# Columns
categorical_cols = ['Geography', 'Gender', 'AGE_group']
numerical_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
binary_cols = ['HasCrCard', 'IsActiveMember']

from sklearn.preprocessing import FunctionTransformer

from utils import add_age_group
age_transformer=FunctionTransformer(add_age_group,validate=False)


# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown='ignore'), categorical_cols),
        ("num", StandardScaler(), numerical_cols),
        ("bin", "passthrough", binary_cols)
    ]
)
# Pipeline
pipeline = Pipeline([
    ("age_feature",age_transformer),
    ("preprocessor", preprocessor),
    ("model", XGBClassifier(subsample= 0.8,scale_pos_weight= 3,n_estimators= 200,max_depth= 3, learning_rate= 0.05,gamma= 0.2,colsample_bytree= 0.7))
])

# Train
pipeline.fit(xtrain, ytrain)

# Save
joblib.dump(pipeline, "churn_pipeline.pkl")