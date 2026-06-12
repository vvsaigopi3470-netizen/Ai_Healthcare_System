import joblib
from flask import Flask, request, render_template

app = Flask(__name__)
staff = app.blueprint('staff', __name__)

model=joblib.load(
'saved_models/staff_model.pkl'
)

def predict_staff(
patients
):

    prediction=model.predict(
    [[patients]]
    )

    return round(
    prediction[0]
    )

@staff.route(
'/forecast_staff',
methods=['GET','POST']
)

def forecast_staff():

    result=None

    if request.method=='POST':

        patients=int(
        request.form[
        'patients'
        ]
        )

        from ml.staff_forecasting \
        import predict_staff

        result=predict_staff(
        patients
        )

    return render_template(
    'staff/forecast_staff.html',
    result=result
    )

