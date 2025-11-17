# Logistic regression only involving two sets binary class
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv('insurance_data.csv')
print(df)

plt.scatter(df.age,df.bought_insurance,marker='o',color='red')
plt.show()

# Splitting the datasets
X_train, X_test, Y_train, Y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.9,test_size=0.1,random_state=42)

model = LogisticRegression()
model.fit(X_train,Y_train)

# This part of the code save the model
with open ('model.pickle', 'wb') as file:
    pickle.dump(model, file)

# This part of the code saves the model
with open('model.pickle', 'rb') as file:
    model_x = pickle.load(file)

prediction = model_x.predict(X_test)
print(X_test)
print(prediction)
print(model_x.score(X_test,Y_test))
print(model_x.predict_proba(X_test))