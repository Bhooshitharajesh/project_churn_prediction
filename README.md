Customer Churn Prediction

Project Overview

This project predicts whether a customer is likely to leave a company (churn) based on customer-related features. The main goal is to help businesses identify potential churn customers early and take preventive actions to improve customer retention.

Problem Statement

Customer churn is one of the major challenges faced by businesses. Losing existing customers can reduce revenue and increase acquisition costs. This project uses Machine Learning techniques to analyze customer behavior and predict churn probability.

Technologies Used

Python ,
Pandas ,
NumPy ,
Matplotlib ,
Seaborn ,
Scikit-learn ,
XGBoost ,
FastAPI ,
Pydantic

Machine Learning Workflow

1. Data Preprocessing :
Handled missing values ,
Encoded categorical features using One-Hot Encoding ,
Scaled numerical features ,
Performed train-test split

2. Exploratory Data Analysis (EDA) :
Analyzed customer behavior patterns ,
Compared features against churn target ,
Visualized important trends using charts and graphs

3. Model Building :
Implemented and compared multiple Machine Learning models like
Logistic Regression ,
Decision Tree Classifier,
Random Forest Classifier ,
XGBoost Classifier

4. Model Optimization :
Performed Hyperparameter Tuning ,
Applied Threshold Tuning ,
Handled class imbalance using :
class_weight='balanced'

6. Model Evaluation :
Evaluation metrics used:
Accuracy ,
Precision ,
Recall ,
F1-Score ,
ROC-AUC Score

    XGBoost achieved the best overall performance for churn prediction.

6. Deployment :
The trained model was deployed using:
FastAPI ,
Swagger UI

The API accepts customer input data and returns churn prediction results in real time.

Live API Deployment
https://project-churn-prediction.onrender.com

Swagger UI
https://project-churn-prediction.onrender.com/docs

Churn prediction swagger UI 

<img width="1907" height="1077" alt="churn prediction swagger UI" src="https://github.com/user-attachments/assets/1684bbcd-41b4-430d-9558-996caca181fb" />

Result of churn prediction

<img width="1918" height="1078" alt="Result of churn prediction" src="https://github.com/user-attachments/assets/eb72348f-3829-47a3-934e-fce2fe866c73" />



