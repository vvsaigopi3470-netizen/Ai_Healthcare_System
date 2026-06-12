def detect_intent(message):

    message = message.lower()

    if "appointment" in message:
        return "appointment"

    elif "fever" in message:
        return "fever"

    elif "cough" in message:
        return "cough"

    elif "diabetes" in message:
        return "diabetes"

    elif "heart" in message:
        return "heart disease"

    elif "medicine" in message:
        return "medicine"

    else:
        return "general"