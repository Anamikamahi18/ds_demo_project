import pandas as pd
import numpy as np


def data_preprocessing(df):
    # Example preprocessing steps
    df = df.dropna()  # Remove missing values
    df = pd.get_dummies(df, drop_first=True)  # One-hot encode categorical variables
    df = df.drop_duplicates()
    df["oldpeak_log"] = np.log1p(df["oldpeak"])
    return df
