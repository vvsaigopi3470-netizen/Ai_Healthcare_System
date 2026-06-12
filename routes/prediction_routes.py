from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import redirect

from database.db import mysql

from ml.disease_predictor import predict_disease

prediction = Blueprint(
    "prediction",
    __name__
)

# =====================================
# Disease Prediction
# =====================================

@prediction.route(
    '/predict_disease',
    methods=['GET', 'POST']
)
def predict():

    if request.method == 'POST':

        try:

            patient_id = int(
                request.form['patient_id']
            )

            age = int(
                request.form['age']
            )

            gender = int(
                request.form['gender']
            )

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

            disease = predict_disease(
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

            # Risk Calculation

            if sugar > 180 or bp > 160:

                risk_score = 90
                severity = "High"

            elif sugar > 140 or bp > 140:

                risk_score = 70
                severity = "Medium"

            else:

                risk_score = 30
                severity = "Low"

            cursor = mysql.connection.cursor()

            cursor.execute(
                """
                INSERT INTO disease_predictions
                (
                    patient_id,
                    predicted_disease,
                    risk_score,
                    severity
                )
                VALUES
                (%s,%s,%s,%s)
                """,
                (
                    patient_id,
                    str(disease),
                    risk_score,
                    severity
                )
            )

            mysql.connection.commit()

            cursor.close()

            return render_template(
                'prediction/prediction_result.html',
                disease=disease,
                risk=risk_score,
                severity=severity
            )

        except Exception as e:

            print("Prediction Error:", e)

            flash(
                f"Prediction Error: {str(e)}",
                "danger"
            )

            return redirect(
                '/predict_disease'
            )

    return render_template(
        'prediction/predict.html'
    )


# =====================================
# Prediction Dashboard
# =====================================

@prediction.route(
    '/prediction_dashboard'
)
def prediction_dashboard():

    cursor = mysql.connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM disease_predictions
        """
    )

    total = cursor.fetchone()[0]

    cursor.close()

    return render_template(
        'prediction/prediction_dashboard.html',
        total=total
    )


# =====================================
# Prediction History
# =====================================

@prediction.route(
    '/prediction_history'
)
def history():

    cursor = mysql.connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM disease_predictions
        ORDER BY prediction_date DESC
        """
    )

    data = cursor.fetchall()

    cursor.close()

    return render_template(
        'prediction/prediction_history.html',
        predictions=data
    )

