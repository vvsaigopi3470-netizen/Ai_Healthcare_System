from os import getenv

try:
    from twilio.rest import Client

    ACCOUNT_SID = getenv(
        'TWILIO_ACCOUNT_SID'
    )

    AUTH_TOKEN = getenv(
        'TWILIO_AUTH_TOKEN'
    )

    if ACCOUNT_SID and AUTH_TOKEN:

        client = Client(
            ACCOUNT_SID,
            AUTH_TOKEN
        )

    else:

        client = None

        print(
            "Twilio credentials not found."
        )

        print(
            "WhatsApp service disabled."
        )

except Exception:

    client = None

    print(
        "Twilio package not available."
    )

    print(
        "WhatsApp service disabled."
    )


def send_whatsapp(
    phone,
    message
):

    if client is None:

        print(
            f"[MOCK WhatsApp] "
            f"{phone} -> {message}"
        )

        return True

    try:

        client.messages.create(

            body=message,

            from_=
            'whatsapp:+14155238886',

            to=
            f'whatsapp:{phone}'

        )

        return True

    except Exception as e:

        print(
            "WhatsApp Error:",
            e
        )

        return False


def send_whatsapp_alert(
    patient_id,
    message
):

    print(
        f"Emergency Alert for "
        f"Patient {patient_id}"
    )

    print(message)

    return True