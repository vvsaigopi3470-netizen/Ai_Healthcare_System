import pandas as pd

from sklearn.linear_model import \
LinearRegression

import joblib

df=pd.read_csv(
'datasets/patient_load.csv'
)

X=df[['Patients']]
y=df['RequiredStaff']

model=LinearRegression()

model.fit(X,y)

joblib.dump(
model,
'saved_models/staff_model.pkl'
)

print(
"Staff Model Trained"
)