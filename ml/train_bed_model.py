import pandas as pd

from sklearn.linear_model import \
LinearRegression

import joblib

df=pd.read_csv(
'datasets/bed_usage.csv'
)

X=df[['Admissions']]
y=df['BedDemand']

model=LinearRegression()

model.fit(X,y)

joblib.dump(
model,
'saved_models/bed_forecast_model.pkl'
)

print(
"Bed Forecast Model Ready"
)