# python
import math
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv('data.csv')

# Drop rows with missing features/target
df = df.dropna(subset=['area', 'room', 'age', 'price'])

# Prepare features and target
X = df[['area', 'room', 'age']].values
y = df['price'].values

# Train model
reg = LinearRegression()
reg.fit(X, y)

# Output coefficients and a prediction
print('coefficients:', reg.coef_)
prediction = reg.predict(np.array([[3000, 3, 40]]))
print(prediction)
