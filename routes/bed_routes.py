from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from database.db import mysql

bed = Blueprint(
'bed',
__name__
)

@bed.route(
'/add_bed',
methods=['GET','POST']
)

def add_bed():

    if request.method == 'POST':

        bed_number = request.form[
        'bed_number'
        ]

        ward_type = request.form[
        'ward_type'
        ]

        cursor=mysql.connection.cursor()

        cursor.execute(
        """
        INSERT INTO beds
        (
        bed_number,
        ward_type,
        status
        )

        VALUES
        (%s,%s,%s)
        """,

        (
        bed_number,
        ward_type,
        "Available"
        )
        )

        mysql.connection.commit()

        return redirect(
        '/bed_dashboard'
        )

    return render_template(
    'beds/add_bed.html'
    )

@bed.route(
'/assign_bed',
methods=['GET','POST']
)

def assign_bed():

    if request.method == 'POST':

        bed_id = request.form[
        'bed_id'
        ]

        patient_id = request.form[
        'patient_id'
        ]

        cursor=mysql.connection.cursor()

        cursor.execute(
        """
        UPDATE beds

        SET
        status='Occupied',
        patient_id=%s

        WHERE bed_id=%s
        """,

        (
        patient_id,
        bed_id
        )
        )

        mysql.connection.commit()

        return redirect(
        '/bed_dashboard'
        )

    return render_template(
    'beds/assign_bed.html'
    )

@bed.route(
'/release_bed/<int:id>'
)

def release_bed(id):

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    UPDATE beds

    SET
    status='Available',
    patient_id=NULL

    WHERE bed_id=%s
    """,

    (id,)
    )

    mysql.connection.commit()

    return redirect(
    '/bed_dashboard'
    )

@bed.route(
'/bed_dashboard'
)

def bed_dashboard():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM beds
    """
    )

    total_beds=cursor.fetchone()[0]

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM beds
    WHERE status='Available'
    """
    )

    available=cursor.fetchone()[0]

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM beds
    WHERE status='Occupied'
    """
    )

    occupied=cursor.fetchone()[0]

    return render_template(

    'beds/bed_dashboard.html',

    total=total_beds,

    available=available,

    occupied=occupied

    )
