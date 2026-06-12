def analyze_report(text):

    risks = []

    if "glucose" in text.lower():
        risks.append(
        "Diabetes Indicator"
        )

    if "cholesterol" in text.lower():
        risks.append(
        "Heart Disease Indicator"
        )

    if "creatinine" in text.lower():
        risks.append(
        "Kidney Disease Indicator"
        )

    if "tumor" in text.lower():
        risks.append(
        "Cancer Indicator"
        )

    if len(risks) == 0:

        risk_level = "Low"

    elif len(risks) <= 2:

        risk_level = "Medium"

    else:

        risk_level = "High"

    return risks, risk_level