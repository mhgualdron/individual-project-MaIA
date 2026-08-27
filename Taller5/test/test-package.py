import pandas as pd
from pathlib import Path
# pyrefly: ignore [missing-import]
from model.predict import make_prediction

_HERE = Path(__file__).parent
sample_input_data = pd.read_csv(_HERE / "bankchurn_test.csv")
result = make_prediction(input_data=sample_input_data)
print(result)