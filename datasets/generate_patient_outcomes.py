import pandas as pd
import random

records = []

for _ in range(250):

    age = random.randint(18, 85)

    gender = random.choice([
        "Male",
        "Female"
    ])

    bp = random.randint(90, 190)

    sugar = random.randint(70, 300)

    bmi = round(
        random.uniform(18, 42),
        1
    )

    cholesterol = random.randint(
        120,
        350
    )

    heart_rate = random.randint(
        55,
        130
    )

    smoking = random.choice([0, 1])

    alcohol = random.choice([0, 1])

    family_history = random.choice([0, 1])

    risk_score = 0

    if age > 60:
        risk_score += 1

    if bp > 150:
        risk_score += 1

    if sugar > 180:
        risk_score += 1

    if bmi > 30:
        risk_score += 1

    if cholesterol > 240:
        risk_score += 1

    if heart_rate > 110:
        risk_score += 1

    if smoking == 1:
        risk_score += 1

    if family_history == 1:
        risk_score += 1

    recovery = 1

    if risk_score >= 4:
        recovery = 0

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
        recovery
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
    "Recovery"
])

df.to_csv(
    "datasets/patient_outcomes.csv",
    index=False
)

print("250 records generated successfully")