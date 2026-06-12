import joblib

model = joblib.load(
    "saved_models/outcome_model.pkl"
)

def predict_outcome(
    age,
    gender,
    bp,
    sugar,
    bmi,
    cholesterol,
    heart_rate,
    smoking,
    alcohol,
    family_history
):

    probability = model.predict_proba([
        [
            age,
            gender,
            bp,
            sugar,
            bmi,
            cholesterol,
            heart_rate,
            smoking,
            alcohol,
            family_history
        ]
    ])

    recovery_prob = round(
        probability[0][1] * 100,
        2
    )

    return recovery_prob