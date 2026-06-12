def send_email_alert(
patient_id,
message
):

    print(
        f"Email Alert Sent "
        f"for Patient {patient_id}"
    )

from flask_mail import Mail, Message

mail = Mail()

def send_email(
recipient,
subject,
body
):

    msg = Message(

        subject,

        recipients=[recipient]

    )

    msg.body = body

    mail.send(msg)

    return True