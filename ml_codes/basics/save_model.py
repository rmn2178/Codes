# IMPORTANT NOTE THIS CODE IS TAKEN FROM THE house_rate/code.py FILE
# SO YOU NEED TO DOWNLOAD THE DATA FROM data.csv FILE SO THAT THE CODE CAN RUN WITHOUT ERRORS
# To save a trained linear regression model you need a module pickle
import pickle
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
print('coefficients:', reg.coef_)

# Here saving the model into the model.pickle
with open('model.pickle', 'wb') as f:
    pickle.dump(reg, f)

# Here loading the model from the model.pickle
with open('model.pickle', 'rb') as f:
    model_x = pickle.load(f)

# Output prediction

prediction = model_x.predict(np.array([[3000, 3, 40]]))
print(prediction)
