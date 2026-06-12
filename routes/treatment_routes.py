from flask import Blueprint
from flask import render_template
from flask import request

from database.db import mysql

from ml.treatment_engine import \
get_recommendation

treatment = Blueprint(
'treatment',
__name__
)

@treatment.route(
'/recommend_treatment',
methods=['GET','POST']
)

def recommend():

    if request.method == 'POST':

        patient_id = request.form[
        'patient_id'
        ]

        disease = request.form[
        'disease'
        ]

        recommendation = \
        get_recommendation(
        disease
        )

        cursor = mysql.connection.cursor()

        cursor.execute(
        """
        INSERT INTO
        treatment_recommendations
        (
        patient_id,
        predicted_disease,
        specialist,
        medications,
        diagnostic_tests,
        lifestyle_advice
        )

        VALUES
        (%s,%s,%s,%s,%s,%s)
        """,

        (
            patient_id,
            disease,
            recommendation[
            "specialist"
            ],

            recommendation[
            "medications"
            ],

            recommendation[
            "tests"
            ],

            recommendation[
            "lifestyle"
            ]
        )
        )

        mysql.connection.commit()

        return render_template(

        'treatment/treatment_result.html',

        disease=disease,

        recommendation=
        recommendation

        )

    return render_template(
    'treatment/recommend.html'
    )

@treatment.route(
'/treatment_dashboard'
)

def dashboard():

    cursor = mysql.connection.cursor()

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM treatment_recommendations
    """
    )

    total = cursor.fetchone()[0]

    return render_template(

    'treatment/treatment_dashboard.html',

    total=total

    )

@treatment.route(
'/treatment_history'
)

def history():

    cursor = mysql.connection.cursor()

    cursor.execute(
    """
    SELECT *
    FROM
    treatment_recommendations
    ORDER BY
    created_at DESC
    """
    )

    data = cursor.fetchall()

    return render_template(

    'treatment/treatment_history.html',

    records=data

    )


