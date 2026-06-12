import schedule
import time

def send_daily_reminders():

    print(
    "Medicine Reminder Sent"
    )

schedule.every().day.at(
"09:00"
).do(
send_daily_reminders
)

def appointment_reminder(patient_name, appointment_date):
    return f"""

    Dear {patient_name},

    Reminder:
    Your appointment is scheduled on

    {appointment_date}

    """


def medicine_reminder(medicine_name, time):
    return f"""

    Reminder:

    Take {medicine_name}

    at {time}

    """


def emergency_alert():
    return """

    Critical Condition Detected

    Immediate Medical Attention
    Required
    """


while True:
    schedule.run_pending()
    time.sleep(60)



