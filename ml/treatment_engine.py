treatment_db = {

"Diabetes": {

"specialist":
"Endocrinologist",

"medications":
"Metformin, Insulin",

"tests":
"HbA1c, Fasting Blood Sugar",

"lifestyle":
"Low Sugar Diet, Daily Exercise"

},

"Heart Disease": {

"specialist":
"Cardiologist",

"medications":
"Aspirin, Statins",

"tests":
"ECG, Echocardiogram",

"lifestyle":
"Low Fat Diet, Walking"

},

"Kidney Disease": {

"specialist":
"Nephrologist",

"medications":
"ACE Inhibitors",

"tests":
"Creatinine Test, Urine Test",

"lifestyle":
"Low Sodium Diet"

},

"Cancer Risk": {

"specialist":
"Oncologist",

"medications":
"Further Evaluation Needed",

"tests":
"Biopsy, MRI, CT Scan",

"lifestyle":
"Stop Smoking, Healthy Diet"

},

"Healthy": {

"specialist":
"General Physician",

"medications":
"No Medication Needed",

"tests":
"Routine Checkup",

"lifestyle":
"Maintain Healthy Lifestyle"

}

}

def get_recommendation(disease):

    return treatment_db.get(
        disease,
        treatment_db["Healthy"]
    )
