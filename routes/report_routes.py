from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from database.db import mysql

from ml.report_analysis \
import extract_text

from ml.medical_nlp \
import analyze_report

import os

report = Blueprint(
'report',
__name__
)

@report.route(
'/upload_report',
methods=['GET','POST']
)

def upload_report():

    if request.method == 'POST':

        patient_id = request.form[
        'patient_id'
        ]

        file = request.files[
        'report'
        ]

        filename = file.filename

        path = os.path.join(
        'uploads/reports',
        filename
        )

        file.save(path)

        extracted_text = \
        extract_text(path)

        issues, risk = \
        analyze_report(
        extracted_text
        )

        cursor = mysql.connection.cursor()

        cursor.execute(
        """
        INSERT INTO
        report_analysis
        (
        patient_id,
        report_name,
        extracted_text,
        risk_level,
        detected_issues
        )

        VALUES
        (%s,%s,%s,%s,%s)
        """,

        (
        patient_id,
        filename,
        extracted_text,
        risk,
        ",".join(issues)
        )
        )

        mysql.connection.commit()

        return render_template(

        'reports/report_result.html',

        text=extracted_text,

        issues=issues,

        risk=risk

        )

    return render_template(
    'reports/upload_report.html'
    )

@report.route(
'/report_dashboard'
)

def dashboard():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM report_analysis
    """
    )

    total=cursor.fetchone()[0]

    return render_template(

    'reports/report_dashboard.html',

    total=total

    )

@report.route(
'/report_history'
)

def history():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT *
    FROM report_analysis
    ORDER BY
    created_at DESC
    """
    )

    data=cursor.fetchall()

    return render_template(
    'reports/report_history.html',
    reports=data
    )