import pandas as pd
import numpy as np
import random

records = []

for _ in range(1500):

    age = random.randint(18, 85)
    gender = random.choice(["Male", "Female"])

    bp = random.randint(90, 190)
    sugar = random.randint(70, 300)
    bmi = round(random.uniform(18, 42), 1)
    cholesterol = random.randint(120, 350)
    heart_rate = random.randint(55, 130)

    smoking = random.choice([0, 1])
    alcohol = random.choice([0, 1])
    family_history = random.choice([0, 1])

    disease = "Healthy"

    if sugar > 180 and bmi > 28:
        disease = "Diabetes"

    elif bp > 150 and cholesterol > 240:
        disease = "Heart Disease"

    elif bp > 140 and sugar > 160 and age > 55:
        disease = "Kidney Disease"

    elif smoking == 1 and age > 50 and family_history == 1:
        disease = "Cancer Risk"

    records.append([
        age,
        gender,
        bp,
        sugar,
        bmi,
        cholesterol,
        heart_rate,
        smoking,
        alcohol,
        family_history,
        disease
    ])

df = pd.DataFrame(records, columns=[
    "Age",
    "Gender",
    "BP",
    "Sugar",
    "BMI",
    "Cholesterol",
    "HeartRate",
    "Smoking",
    "Alcohol",
    "FamilyHistory",
    "Disease"
])

df.to_csv(
    "datasets/healthcare_dataset.csv",
    index=False
)

print("1500 records generated successfully")