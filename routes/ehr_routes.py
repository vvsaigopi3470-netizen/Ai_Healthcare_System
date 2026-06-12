from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash

from database.db import mysql

import os

ehr = Blueprint(
    "ehr",
    __name__
)

@ehr.route(
'/add_record',
methods=['GET','POST']
)

def add_record():

    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT patient_id,name FROM patients"
    )

    patients = cursor.fetchall()

    cursor.execute(
        "SELECT doctor_id,name FROM doctors"
    )

    doctors = cursor.fetchall()

    if request.method == 'POST':

        patient_id = request.form['patient_id']

        doctor_id = request.form['doctor_id']

        diagnosis = request.form['diagnosis']

        prescription = request.form[
            'prescription'
        ]

        treatment_history = request.form[
            'treatment_history'
        ]

        vaccination_record = request.form[
            'vaccination_record'
        ]

        doctor_notes = request.form[
            'doctor_notes'
        ]

        report = request.files['report']

        filename = report.filename

        report.save(
            os.path.join(
                'uploads/medical_reports',
                filename
            )
        )

        cursor.execute(
        """
        INSERT INTO ehr_records
        (
        patient_id,
        doctor_id,
        diagnosis,
        prescription,
        treatment_history,
        vaccination_record,
        doctor_notes,
        report_file
        )

        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s)
        """,

        (
            patient_id,
            doctor_id,
            diagnosis,
            prescription,
            treatment_history,
            vaccination_record,
            doctor_notes,
            filename
        )
        )

        mysql.connection.commit()

        flash(
        "Medical Record Saved"
        )

        return redirect(
        '/ehr_dashboard'
        )

    return render_template(
        "ehr/add_record.html",
        patients=patients,
        doctors=doctors
    )

@ehr.route('/ehr_dashboard')

def ehr_dashboard():

    cursor=mysql.connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM ehr_records"
    )

    total=cursor.fetchone()[0]

    return render_template(
        "ehr/ehr_dashboard.html",
        total=total
    )

@ehr.route('/ehr_records')

def ehr_records():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT
    e.record_id,
    p.name,
    d.name,
    e.created_at

    FROM ehr_records e

    JOIN patients p

    ON e.patient_id=p.patient_id

    JOIN doctors d

    ON e.doctor_id=d.doctor_id
    """
    )

    data=cursor.fetchall()

    return render_template(
    "ehr/ehr_list.html",
    records=data
    )

@ehr.route(
'/ehr/<int:id>'
)

def ehr_details(id):

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT *
    FROM ehr_records
    WHERE record_id=%s
    """,

    (id,)
    )

    record=cursor.fetchone()

    return render_template(
    "ehr/ehr_details.html",
    record=record
    )

@ehr.route(
'/delete_record/<int:id>'
)

def delete_record(id):

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    DELETE FROM ehr_records
    WHERE record_id=%s
    """,

    (id,)
    )

    mysql.connection.commit()

    return redirect(
    '/ehr_records'
    )