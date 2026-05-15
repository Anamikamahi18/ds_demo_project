import pandas as pd
from src.helper import load_config
from src.data_preprocessing import data_preprocessing

config = load_config()
raw_data_path = config["raw_data_path"]
data = pd.read_csv(raw_data_path)
data = data_preprocessing(data)
data.to_csv(config["preprocessed_data_path"], index=False)
print(data.head())
