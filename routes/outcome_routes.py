from flask import Blueprint
from flask import render_template
from flask import request

from database.db import mysql

from ml.outcome_predictor import \
predict_outcome

outcome = Blueprint(
'outcome',
__name__
)

@outcome.route(
'/predict_outcome',
methods=['GET','POST']
)

def predict():

    if request.method == 'POST':

        patient_id = int(
        request.form['patient_id']
        )

        age = int(
        request.form['age']
        )

        gender = request.form['gender']

        bp = int(
        request.form['bp']
        )

        sugar = int(
        request.form['sugar']
        )

        bmi = float(
        request.form['bmi']
        )

        cholesterol = int(
        request.form['cholesterol']
        )

        heart_rate = int(
        request.form['heart_rate']
        )

        smoking = int(
        request.form['smoking']
        )

        alcohol = int(
        request.form['alcohol']
        )

        family_history = int(
        request.form['family_history']
        )

        recovery = predict_outcome(
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
        )

        icu_risk = round(
        (100 - recovery) * 0.60,
        2
        )

        readmission_risk = round(
        (100 - recovery) * 0.40,
        2
        )

        mortality_risk = round(
        (100 - recovery) * 0.25,
        2
        )

        expected_stay = max(
        1,
        int((100-recovery)/10)
        )

        if recovery > 80:
            risk = "Low"

        elif recovery > 50:
            risk = "Medium"

        else:
            risk = "High"

        cursor = mysql.connection.cursor()

        cursor.execute(
        """
        INSERT INTO patient_outcomes
        (
        patient_id,
        recovery_probability,
        icu_risk,
        readmission_risk,
        mortality_risk,
        expected_stay,
        risk_level
        )

        VALUES
        (%s,%s,%s,%s,%s,%s,%s)
        """,

        (
        patient_id,
        recovery,
        icu_risk,
        readmission_risk,
        mortality_risk,
        expected_stay,
        risk
        )
        )

        mysql.connection.commit()

        return render_template(

        'outcome/outcome_result.html',

        recovery=recovery,

        icu=icu_risk,

        readmission=
        readmission_risk,

        mortality=
        mortality_risk,

        stay=
        expected_stay,

        risk=risk

        )

    return render_template(
    'outcome/predict_outcome.html'
    )

@outcome.route(
'/outcome_dashboard'
)

def dashboard():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM patient_outcomes
    """
    )

    total=cursor.fetchone()[0]

    return render_template(
    'outcome/outcome_dashboard.html',
    total=total
    )

@outcome.route(
'/outcome_history'
)

def history():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT *
    FROM patient_outcomes
    ORDER BY created_at DESC
    """
    )

    data=cursor.fetchall()

    return render_template(
    'outcome/outcome_history.html',
    outcomes=data
    )

