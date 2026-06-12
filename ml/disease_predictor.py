import joblib

model = joblib.load(
'saved_models/disease_model.pkl'
)

def predict_disease(
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

    prediction = model.predict(
    [[
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
    ]]
    )

    return prediction[0]