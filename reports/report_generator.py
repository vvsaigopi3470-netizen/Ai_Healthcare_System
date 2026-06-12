from database.db import mysql

def disease_report():

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

    return cursor.fetchall()

def recovery_report():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT
    patient_id,
    recovery_probability

    FROM patient_outcomes
    """
    )

    return cursor.fetchall()

def doctor_report():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT
    doctor_id,
    COUNT(*)

    FROM consultation_notes

    GROUP BY doctor_id
    """
    )

    return cursor.fetchall()

def bed_report():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT
    status,
    COUNT(*)

    FROM beds

    GROUP BY status
    """
    )

    return cursor.fetchall()

def resource_report():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT
    resource_name,
    available_quantity

    FROM hospital_resources
    """
    )

    return cursor.fetchall()

def revenue_report():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT *
    FROM hospital_revenue
    """
    )

    return cursor.fetchall()