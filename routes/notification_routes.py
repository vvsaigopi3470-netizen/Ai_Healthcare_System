from flask import Blueprint
from flask import render_template
from flask import request

from database.db import mysql

from notifications.email_service \
import send_email

notification = Blueprint(
'notification',
__name__
)

@notification.route(
'/send_notification',
methods=['GET','POST']
)

def send_notification():

    if request.method=='POST':

        patient_id=request.form[
        'patient_id'
        ]

        email=request.form[
        'email'
        ]

        title=request.form[
        'title'
        ]

        message=request.form[
        'message'
        ]

        send_email(
        email,
        title,
        message
        )

        cursor=mysql.connection.cursor()

        cursor.execute(
        """
        INSERT INTO notifications
        (
        patient_id,
        channel,
        title,
        message,
        status
        )

        VALUES
        (%s,%s,%s,%s,%s)
        """,

        (
        patient_id,
        "Email",
        title,
        message,
        "Sent"
        )
        )

        mysql.connection.commit()

        return "Notification Sent"

    return render_template(
    'notifications/send_notification.html'
    )

def appointment_reminder(
patient_name,
appointment_date
):

    return f"""

    Dear {patient_name},

    Reminder:
    Your appointment is scheduled on

    {appointment_date}

    """

@notification.route(
'/notification_dashboard'
)

def dashboard():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM notifications
    """
    )

    total=cursor.fetchone()[0]

    return render_template(
    'notifications/notification_dashboard.html',
    total=total
    )

@notification.route(
'/notification_history'
)

def history():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT *
    FROM notifications
    ORDER BY created_at DESC
    """
    )

    data=cursor.fetchall()

    return render_template(
    'notifications/notification_history.html',
    notifications=data
    )