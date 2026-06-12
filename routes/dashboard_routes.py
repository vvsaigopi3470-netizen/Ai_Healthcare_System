from flask import Blueprint
from flask import render_template

from database.db import mysql

dashboard = Blueprint(
'dashboard',
__name__
)

@dashboard.route(
'/admin_dashboard'
)

def admin_dashboard():

    cursor=mysql.connection.cursor()

    cursor.execute(
    "SELECT COUNT(*) FROM patients"
    )
    patients=cursor.fetchone()[0]

    cursor.execute(
    "SELECT COUNT(*) FROM doctors"
    )
    doctors=cursor.fetchone()[0]

    cursor.execute(
    "SELECT COUNT(*) FROM appointments"
    )
    appointments=cursor.fetchone()[0]

    cursor.execute(
    "SELECT COUNT(*) FROM beds"
    )
    beds=cursor.fetchone()[0]

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM beds
    WHERE status='Occupied'
    """
    )
    occupied=cursor.fetchone()[0]

    return render_template(

    'dashboard/admin_dashboard.html',

    patients=patients,

    doctors=doctors,

    appointments=appointments,

    beds=beds,

    occupied=occupied

    )

@dashboard.route(
'/doctor_dashboard_view'
)

def doctor_dashboard():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM consultation_notes
    """
    )

    consultations=cursor.fetchone()[0]

    return render_template(
    'dashboard/doctor_dashboard.html',
    consultations=consultations
    )

@dashboard.route(
'/patient_dashboard_view'
)

def patient_dashboard():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM ehr_records
    """
    )

    records=cursor.fetchone()[0]

    return render_template(
    'dashboard/patient_dashboard.html',
    records=records
    )

@dashboard.route(
'/disease_statistics'
)

def disease_statistics():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT
    predicted_disease,
    COUNT(*)

    FROM disease_predictions

    GROUP BY
    predicted_disease
    """
    )

    data=cursor.fetchall()

    labels=[]
    values=[]

    for row in data:

        labels.append(row[0])

        values.append(row[1])

    return {
        "labels": labels,
        "values": values
    }

@dashboard.route(
'/bed_statistics'
)

def bed_statistics():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT status,
    COUNT(*)

    FROM beds

    GROUP BY status
    """
    )

    data=cursor.fetchall()

    return {
    "data": data
    }

@dashboard.route(
'/recovery_statistics'
)

def recovery_stats():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT AVG(
    recovery_probability
    )

    FROM patient_outcomes
    """
    )

    avg_recovery=cursor.fetchone()[0]

    return {
    "average_recovery":
    avg_recovery
    }

@dashboard.route(
'/staff_statistics'
)

def staff_statistics():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT role,
    COUNT(*)

    FROM staff

    GROUP BY role
    """
    )

    data=cursor.fetchall()

    return {
    "staff_data":data
    }

@dashboard.route(
'/analytics'
)

def analytics():

    return render_template(
    'dashboard/analytics.html'
    )
