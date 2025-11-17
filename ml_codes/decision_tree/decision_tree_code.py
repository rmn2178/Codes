import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

# The df contains Company,Job,Degree,Salary_more_then_100k
# Loading the data into the df
df = pd.read_csv('salaries.csv')

# Here we are dropping the Salary_more_then_100k
# Here we are separating the inputs and the target
inputs = df.drop("Salary_more_then_100k",axis="columns")
target = df['Salary_more_then_100k']

# We are making the data into numbers so machine can understand
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company_x'] = le_company.fit_transform(inputs['Company'])
inputs['job_x'] = le_company.fit_transform(inputs['Job'])
inputs['degree_x'] = le_company.fit_transform(inputs['Degree'])

print(inputs.head())

# Here the inputs are changed to numbers but it was converted into 6 frames
# But we need only three so deleting the first three
# Here we are using the drop function
inputs_x = inputs.drop(['Company','Job','Degree'],axis="columns")
print(inputs_x.head())

# Here we are training the model
model = tree.DecisionTreeClassifier()
model.fit(inputs_x,target)

print(model.predict([[2,2,1]]))