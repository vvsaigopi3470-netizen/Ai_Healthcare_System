from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash

from database.db import mysql

appointment = Blueprint(
    "appointment",
    __name__
)

@appointment.route(
'/book_appointment',
methods=['GET','POST']
)

def book_appointment():

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

        appointment_date = request.form[
            'appointment_date'
        ]

        appointment_time = request.form[
            'appointment_time'
        ]

        reason = request.form['reason']

        cursor.execute(
        """
        INSERT INTO appointments
        (
        patient_id,
        doctor_id,
        appointment_date,
        appointment_time,
        status,
        reason
        )

        VALUES
        (%s,%s,%s,%s,%s,%s)
        """,

        (
            patient_id,
            doctor_id,
            appointment_date,
            appointment_time,
            "Pending",
            reason
        )
        )

        mysql.connection.commit()

        flash(
            "Appointment Requested"
        )

        return redirect(
            '/appointment_dashboard'
        )

    return render_template(

        "appointment/book_appointment.html",

        patients=patients,
        doctors=doctors

    )

@appointment.route(
'/appointment_dashboard'
)

def appointment_dashboard():

    cursor = mysql.connection.cursor()

    cursor.execute(
    "SELECT COUNT(*) FROM appointments"
    )

    total = cursor.fetchone()[0]

    return render_template(

        "appointment/appointment_dashboard.html",

        total=total

    )

@appointment.route('/appointments')

def appointments():

    cursor = mysql.connection.cursor()

    cursor.execute(

    """
    SELECT
    a.appointment_id,
    p.name,
    d.name,
    a.appointment_date,
    a.appointment_time,
    a.status

    FROM appointments a

    JOIN patients p
    ON a.patient_id=p.patient_id

    JOIN doctors d
    ON a.doctor_id=d.doctor_id
    """

    )

    data = cursor.fetchall()

    return render_template(

    "appointment/appointment_list.html",

    appointments=data

    )

@appointment.route(
'/appointment/<int:id>'
)

def appointment_details(id):

    cursor = mysql.connection.cursor()

    cursor.execute(

    """
    SELECT *
    FROM appointments
    WHERE appointment_id=%s
    """,

    (id,)
    )

    data = cursor.fetchone()

    return render_template(

    "appointment/appointment_details.html",

    appointment=data

    )

@appointment.route(
'/approve/<int:id>'
)

def approve(id):

    cursor = mysql.connection.cursor()

    cursor.execute(

    """
    UPDATE appointments
    SET status='Approved'
    WHERE appointment_id=%s
    """,

    (id,)
    )

    mysql.connection.commit()

    flash(
    "Appointment Approved"
    )

    return redirect('/appointments')

@appointment.route(
'/reject/<int:id>'
)

def reject(id):

    cursor = mysql.connection.cursor()

    cursor.execute(

    """
    UPDATE appointments
    SET status='Rejected'
    WHERE appointment_id=%s
    """,

    (id,)
    )

    mysql.connection.commit()

    flash(
    "Appointment Rejected"
    )

    return redirect('/appointments')

@appointment.route(
'/reschedule/<int:id>',
methods=['GET','POST']
)

def reschedule(id):

    if request.method == 'POST':

        new_date=request.form['date']
        new_time=request.form['time']

        cursor=mysql.connection.cursor()

        cursor.execute(

        """
        UPDATE appointments

        SET appointment_date=%s,
        appointment_time=%s

        WHERE appointment_id=%s
        """,

        (
        new_date,
        new_time,
        id
        )
        )

        mysql.connection.commit()

        return redirect(
        '/appointments'
        )

    return '''
    <form method="POST">
    Date:
    <input type="date" name="date">
    Time:
    <input type="time" name="time">
    <button>Save</button>
    </form>
    '''