from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash

from database.db import mysql

import os

patient = Blueprint(
    "patient",
    __name__
)

@patient.route(
    '/add_patient',
    methods=['GET','POST']
)

def add_patient():

    if request.method == 'POST':

        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        weight = request.form['weight']
        height = request.form['height']
        blood_group = request.form['blood_group']

        medical_history = request.form[
            'medical_history'
        ]

        allergies = request.form[
            'allergies'
        ]

        family_history = request.form[
            'family_history'
        ]

        insurance_details = request.form[
            'insurance_details'
        ]

        report = request.files['report']

        filename = report.filename

        report.save(
            os.path.join(
                "uploads/reports",
                filename
            )
        )

        cursor = mysql.connection.cursor()

        query = """
        INSERT INTO patients
        (
        name,
        age,
        gender,
        weight,
        height,
        blood_group,
        medical_history,
        allergies,
        family_history,
        insurance_details,
        report_file
        )

        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (

            name,
            age,
            gender,
            weight,
            height,
            blood_group,
            medical_history,
            allergies,
            family_history,
            insurance_details,
            filename

        )

        cursor.execute(
            query,
            values
        )

        mysql.connection.commit()

        flash(
            "Patient Added Successfully"
        )

        return redirect(
            '/patient_dashboard'
        )

    return render_template(
        'patient/add_patient.html'
    )

@patient.route(
    '/patient_dashboard'
)

def patient_dashboard():

    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM patients"
    )

    total_patients = cursor.fetchone()[0]

    return render_template(

        "patient/patient_dashboard.html",

        total_patients=
        total_patients

    )

@patient.route('/patients')

def patients():

    cursor = mysql.connection.cursor()

    cursor.execute(

        "SELECT * FROM patients"

    )

    data = cursor.fetchall()

    return render_template(

        "patient/patient_list.html",

        patients=data

    )

@patient.route(
'/patient/<int:id>'
)

def patient_profile(id):

    cursor = mysql.connection.cursor()

    cursor.execute(

        """
        SELECT *
        FROM patients
        WHERE patient_id=%s
        """,

        (id,)
    )

    patient_data = cursor.fetchone()

    return render_template(

        "patient/patient_profile.html",

        patient=patient_data

    )

@patient.route(
'/delete_patient/<int:id>'
)

def delete_patient(id):

    cursor = mysql.connection.cursor()

    cursor.execute(

        """
        DELETE FROM patients
        WHERE patient_id=%s
        """,

        (id,)
    )

    mysql.connection.commit()

    flash(
        "Patient Deleted"
    )

    return redirect(
        '/patients'
    )