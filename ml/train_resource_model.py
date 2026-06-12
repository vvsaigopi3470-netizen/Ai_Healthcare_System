import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv(
    "datasets/resource_data.csv"
)

X = df[
    [
        "beds",
        "ventilators",
        "oxygen_units"
    ]
]

y = df["resource_demand"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(
    model,
    "saved_models/resource_allocation_model.pkl"
)

print("Resource Model Trained")