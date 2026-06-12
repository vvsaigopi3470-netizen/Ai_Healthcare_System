from flask import Blueprint
from flask import render_template
from database.db import mysql

report_export = Blueprint(
'report_export',
__name__
)

@report_export.route(
'/export_disease_report'
)

def export_disease():

    from reports.report_generator \
    import disease_report

    from reports.excel_export \
    import export_excel

    data=disease_report()

    filepath=export_excel(
    data,
    'disease_report'
    )

    return f"""
    Report Generated:
    {filepath}
    """

@report_export.route(
'/export_recovery_report'
)

def export_recovery():

    from reports.report_generator \
    import recovery_report

    from reports.excel_export \
    import export_excel

    data=recovery_report()

    filepath=export_excel(
    data,
    'recovery_report'
    )

    return filepath

@report_export.route(
'/export_doctor_report'
)

def export_doctor():

    from reports.report_generator \
    import doctor_report

    from reports.excel_export \
    import export_excel

    data=doctor_report()

    filepath=export_excel(
    data,
    'doctor_report'
    )

    return filepath

@report_export.route(
'/export_bed_report'
)

def export_bed():

    from reports.report_generator \
    import bed_report

    from reports.excel_export \
    import export_excel

    data=bed_report()

    filepath=export_excel(
    data,
    'bed_report'
    )

    return filepath

@report_export.route(
'/export_resource_report'
)

def export_resource():

    from reports.report_generator \
    import resource_report

    from reports.excel_export \
    import export_excel

    data=resource_report()

    filepath=export_excel(
    data,
    'resource_report'
    )

    return filepath

@report_export.route(
'/export_pdf_report'
)

def export_pdf_report():

    from reports.pdf_export \
    import export_pdf

    filepath=export_pdf(

    "Hospital Report",

    "Hospital Analytics Summary",

    "hospital_report"

    )

    return filepath

@report_export.route(
'/reports_dashboard'
)

@report_export.route('/report_list')

def report_list():

    cursor = mysql.connection.cursor()

    cursor.execute("""
        SELECT *
        FROM generated_reports
        ORDER BY generated_at DESC
    """)

    reports = cursor.fetchall()

    return render_template(
        'reports_export/report_list.html',
        reports=reports
    )

def reports_dashboard():

    return render_template(
    'reports_export/reports_dashboard.html'
    )