from flask import Blueprint
from flask import render_template
from flask import request

from database.db import mysql

from ml.emergency_monitor \
import analyze_patient

from notifications.email_service \
import send_email_alert

from notifications.sms_service \
import send_sms_alert

from notifications.whatsapp_service \
import send_whatsapp_alert

emergency = Blueprint(
'emergency',
__name__
)

@emergency.route(
'/monitor_patient',
methods=['GET','POST']
)

def monitor():

    if request.method=='POST':

        patient_id=int(
        request.form['patient_id']
        )

        oxygen=float(
        request.form['oxygen']
        )

        heart_rate=float(
        request.form['heart_rate']
        )

        bp=float(
        request.form['bp']
        )

        temperature=float(
        request.form['temperature']
        )

        alerts,severity = \
        analyze_patient(
        oxygen,
        heart_rate,
        bp,
        temperature
        )

        cursor=mysql.connection.cursor()

        cursor.execute(
        """
        INSERT INTO
        patient_monitoring
        (
        patient_id,
        oxygen_level,
        heart_rate,
        blood_pressure,
        temperature
        )

        VALUES
        (%s,%s,%s,%s,%s)
        """,

        (
        patient_id,
        oxygen,
        heart_rate,
        bp,
        temperature
        )
        )

        if len(alerts)>0:

            cursor.execute(
            """
            INSERT INTO
            emergency_alerts
            (
            patient_id,
            oxygen_level,
            heart_rate,
            blood_pressure,
            temperature,
            alert_type,
            severity,
            status
            )

            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s)
            """,

            (
            patient_id,
            oxygen,
            heart_rate,
            bp,
            temperature,
            ",".join(alerts),
            severity,
            "Active"
            )
            )

            send_email_alert(
            patient_id,
            ",".join(alerts)
            )

            send_sms_alert(
            patient_id,
            ",".join(alerts)
            )

            send_whatsapp_alert(
            patient_id,
            ",".join(alerts)
            )

        mysql.connection.commit()

        return render_template(

        'emergency/alert_result.html',

        alerts=alerts,

        severity=severity

        )

    return render_template(
    'emergency/monitor_patient.html'
    )

@emergency.route(
'/emergency_dashboard'
)

def dashboard():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM emergency_alerts
    """
    )

    total=cursor.fetchone()[0]

    return render_template(
    'emergency/emergency_dashboard.html',
    total=total
    )

@emergency.route(
'/emergency_history'
)

def history():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT *
    FROM emergency_alerts
    ORDER BY created_at DESC
    """
    )

    data=cursor.fetchall()

    return render_template(
    'emergency/emergency_history.html',
    alerts=data
    )