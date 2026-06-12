def analyze_patient(
oxygen,
heart_rate,
bp,
temperature
):

    alerts=[]

    severity="Low"

    if oxygen < 90:

        alerts.append(
        "Critical Oxygen Level"
        )

        severity="High"

    if heart_rate > 120:

        alerts.append(
        "Abnormal Heart Rate"
        )

    if bp > 180:

        alerts.append(
        "Critical Blood Pressure"
        )

        severity="High"

    if temperature > 39:

        alerts.append(
        "High Fever"
        )

    return alerts,severity