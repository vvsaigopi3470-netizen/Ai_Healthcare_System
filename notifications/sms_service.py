def send_sms_alert(
patient_id,
message
):

    print(
    f"SMS Alert Sent "
    f"for Patient {patient_id}"
    )

from twilio.rest import Client

# Twilio configuration - replace with real credentials or load from env
ACCOUNT_SID = "YOUR_SID"
AUTH_TOKEN = "YOUR_TOKEN"

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms(
phone,
message
):

    client.messages.create(

    body=message,

    from_="+123456789",

    to=phone

    )