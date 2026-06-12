from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from database.db import mysql

staff = Blueprint(
'staff',
__name__
)

@staff.route(
'/add_staff',
methods=['GET','POST']
)

def add_staff():

    if request.method == 'POST':

        name=request.form['name']
        role=request.form['role']
        department=request.form['department']
        phone=request.form['phone']
        email=request.form['email']

        cursor=mysql.connection.cursor()

        cursor.execute(
        """
        INSERT INTO staff
        (
        name,
        role,
        department,
        phone,
        email,
        availability,
        shift_time
        )

        VALUES
        (%s,%s,%s,%s,%s,%s,%s)
        """,

        (
        name,
        role,
        department,
        phone,
        email,
        "Available",
        "Not Assigned"
        )
        )

        mysql.connection.commit()

        return redirect(
        '/staff_dashboard'
        )

    return render_template(
    'staff/add_staff.html'
    )

@staff.route('/staff_list')

def staff_list():

    cursor=mysql.connection.cursor()

    cursor.execute(
    "SELECT * FROM staff"
    )

    data=cursor.fetchall()

    return render_template(
    'staff/staff_list.html',
    staff=data
    )

@staff.route(
'/assign_shift',
methods=['GET','POST']
)

def assign_shift():

    if request.method=='POST':

        staff_id=request.form[
        'staff_id'
        ]

        shift=request.form[
        'shift'
        ]

        cursor=mysql.connection.cursor()

        cursor.execute(
        """
        UPDATE staff

        SET shift_time=%s

        WHERE staff_id=%s
        """,

        (
        shift,
        staff_id
        )
        )

        mysql.connection.commit()

        return redirect(
        '/staff_dashboard'
        )

    return render_template(
    'staff/assign_shift.html'
    )

@staff.route(
'/attendance',
methods=['GET','POST']
)

def attendance():

    if request.method=='POST':

        staff_id=request.form[
        'staff_id'
        ]

        status=request.form[
        'status'
        ]

        cursor=mysql.connection.cursor()

        cursor.execute(
        """
        INSERT INTO attendance
        (
        staff_id,
        attendance_date,
        status
        )

        VALUES
        (
        %s,
        CURDATE(),
        %s
        )
        """,

        (
        staff_id,
        status
        )
        )

        mysql.connection.commit()

    return render_template(
    'staff/attendance.html'
    )

@staff.route(
'/staff_dashboard'
)

def dashboard():

    cursor=mysql.connection.cursor()

    cursor.execute(
    "SELECT COUNT(*) FROM staff"
    )

    total=cursor.fetchone()[0]

    return render_template(
    'staff/staff_dashboard.html',
    total=total
    )