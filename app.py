from flask import Flask
from flask import render_template

from database.db import mysql
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# Create App
# -----------------------------

app = Flask(__name__)

app.secret_key = "healthcare_secret_key"

import os

# -----------------------------
# MySQL Configuration
# -----------------------------

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT', 3306))

mysql.init_app(app)

# -----------------------------
# Import Blueprints
# -----------------------------

from routes.auth_routes import auth

from routes.patient_routes import patient

from routes.doctor_routes import doctor

from routes.appointment_routes import appointment

from routes.ehr_routes import ehr

from routes.prediction_routes import prediction

from routes.treatment_routes import treatment

from routes.outcome_routes import outcome

from routes.bed_routes import bed

from routes.staff_routes import staff

from routes.resource_routes import resource

from routes.report_routes import report

from routes.emergency_routes import emergency

from routes.chatbot_routes import chatbot

from routes.dashboard_routes import dashboard

from routes.notification_routes import notification

from routes.report_export_routes import report_export

# -----------------------------
# Register Blueprints
# -----------------------------

app.register_blueprint(auth)

app.register_blueprint(patient)

app.register_blueprint(doctor)

app.register_blueprint(appointment)

app.register_blueprint(ehr)

app.register_blueprint(prediction)

app.register_blueprint(treatment)

app.register_blueprint(outcome)

app.register_blueprint(bed)

app.register_blueprint(staff)

app.register_blueprint(resource)

app.register_blueprint(report)

app.register_blueprint(emergency)

app.register_blueprint(chatbot)

app.register_blueprint(dashboard)

app.register_blueprint(notification)

app.register_blueprint(report_export)

# -----------------------------
# Home Page
# -----------------------------

@app.route('/')
def home():

    return render_template(
        'login.html'
    )

# -----------------------------
# Health Check
# -----------------------------

@app.route('/health')
def health():

    return {
        "status": "running",
        "project":
        "AI Healthcare System"
    }

# -----------------------------
# Print All Routes
# -----------------------------

print("\nRegistered Routes:\n")

print(app.url_map)

# -----------------------------
# Run Server
# -----------------------------

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )