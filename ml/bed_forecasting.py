import joblib
from flask import render_template, request, Blueprint

bed = Blueprint('bed', __name__)

model=joblib.load(
'saved_models/bed_forecast_model.pkl'
)

def predict_beds(
admissions
):

    demand=model.predict(
    [[admissions]]
    )

    return round(
    demand[0]
    )

@bed.route(
'/forecast_beds',
methods=['GET','POST']
)

def forecast():

    prediction=None

    if request.method=='POST':

        admissions=int(
        request.form[
        'admissions'
        ]
        )

        from ml.bed_forecasting import predict_beds

        prediction = predict_beds(admissions)

    return render_template(
    'beds/forecast.html',
    prediction=prediction
    )

