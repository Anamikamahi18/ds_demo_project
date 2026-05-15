import pandas as pd


def data_preprocessing(df):
    # Example preprocessing steps
    df = df.dropna()  # Remove missing values
    df = pd.get_dummies(df, drop_first=True)  # One-hot encode categorical variables
    return df
