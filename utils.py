import pandas as pd

def add_age_group(X):
    X = X.copy()
    X['AGE_group'] = pd.cut(
        X['Age'],
        bins=[18, 40, 60, 100],
        labels=['young', 'adult', 'senior'],
        include_lowest=True
    )
    return X