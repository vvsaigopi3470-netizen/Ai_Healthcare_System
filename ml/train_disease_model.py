import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load Dataset
df = pd.read_csv("datasets/healthcare_dataset.csv")

# Convert Gender to Numeric
le_gender = LabelEncoder()
df["Gender"] = le_gender.fit_transform(df["Gender"])

# Features
X = df[
    [
        "Age",
        "Gender",
        "BP",
        "Sugar",
        "BMI",
        "Cholesterol",
        "HeartRate",
        "Smoking",
        "Alcohol",
        "FamilyHistory"
    ]
]

# Target
y = df["Disease"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Save Model
joblib.dump(
    model,
    "saved_models/disease_model.pkl"
)

print("Disease Model Saved Successfully")