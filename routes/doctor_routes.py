from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash

from database.db import mysql

doctor = Blueprint(
    "doctor",
    __name__
)

@doctor.route(
    '/add_doctor',
    methods=['GET','POST']
)

def add_doctor():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        specialization = request.form['specialization']
        department = request.form['department']
        experience = request.form['experience']
        qualification = request.form['qualification']
        phone = request.form['phone']
        available_slots = request.form['available_slots']
        fee = request.form['consultation_fee']

        cursor = mysql.connection.cursor()

        query = """
        INSERT INTO doctors
        (
        name,
        email,
        specialization,
        department,
        experience,
        qualification,
        phone,
        available_slots,
        consultation_fee
        )

        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (

            name,
            email,
            specialization,
            department,
            experience,
            qualification,
            phone,
            available_slots,
            fee

        )

        cursor.execute(
            query,
            values
        )

        mysql.connection.commit()

        flash(
            "Doctor Added Successfully"
        )

        return redirect(
            '/doctor_dashboard'
        )

    return render_template(
        'doctor/add_doctor.html'
    )

@doctor.route(
    '/doctor_dashboard'
)

def doctor_dashboard():

    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM doctors"
    )

    total_doctors = cursor.fetchone()[0]

    return render_template(

        "doctor/doctor_dashboard.html",

        total_doctors=
        total_doctors

    )

@doctor.route('/doctors')

def doctors():

    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT * FROM doctors"
    )

    data = cursor.fetchall()

    return render_template(
        "doctor/doctor_list.html",
        doctors=data
    )

@doctor.route(
'/doctor/<int:id>'
)

def doctor_profile(id):

    cursor = mysql.connection.cursor()

    cursor.execute(

        """
        SELECT *
        FROM doctors
        WHERE doctor_id=%s
        """,

        (id,)
    )

    doctor_data = cursor.fetchone()

    return render_template(

        "doctor/doctor_profile.html",

        doctor=doctor_data

    )

@doctor.route(
'/delete_doctor/<int:id>'
)

def delete_doctor(id):

    cursor = mysql.connection.cursor()

    cursor.execute(

        """
        DELETE FROM doctors
        WHERE doctor_id=%s
        """,

        (id,)
    )

    mysql.connection.commit()

    flash(
        "Doctor Deleted"
    )

    return redirect(
        '/doctors'
    )

@doctor.route(
'/add_consultation',
methods=['POST']
)

def add_consultation():

    doctor_id = request.form['doctor_id']
    patient_id = request.form['patient_id']
    diagnosis = request.form['diagnosis']
    prescription = request.form['prescription']
    remarks = request.form['remarks']

    cursor = mysql.connection.cursor()

    cursor.execute(

    """
    INSERT INTO consultation_notes
    (
    doctor_id,
    patient_id,
    diagnosis,
    prescription,
    remarks
    )

    VALUES
    (%s,%s,%s,%s,%s)
    """,

    (
        doctor_id,
        patient_id,
        diagnosis,
        prescription,
        remarks
    )

    )

    mysql.connection.commit()

    return "Consultation Saved"