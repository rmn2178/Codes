import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
import seaborn as sn

scaler = StandardScaler()  # Loading the scaler for data scaling to avoid errors
digits = load_digits()     # Loading the digits

# This prints the directories of the images
# ['DESCR', 'data', 'feature_names', 'frame', 'images', 'target', 'target_names']
# The above bracket shows the directory
print(dir(digits))

# To print the digits of the data
print(digits.data[0])

# The images show the image of the sample
# To print the sample image
# Take it out of the comments only if you need to see the images
'''
plt.gray()
for i in range(5):
    print(digits.target[i])
    plt.matshow(digits.images[i])
    plt.show()
'''

# We are splitting the training data and the testing data
X_train, X_test, Y_train, Y_test = train_test_split(digits.data, digits.target, test_size=0.1, random_state=42)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# After splitting the data we are training a ml model with the train dataset
model = LogisticRegression(solver='liblinear')
model.fit(X_train, Y_train)

# Getting the probability of the model
print(f"Accuracy {model.score(X_test, Y_test)}")

Y_pred = model.predict(X_test)
con_mat = confusion_matrix(Y_test, Y_pred)
print("The confusion matrix")
print(con_mat)

# Here the works of seaborn
# Here visualising the confusion matrix
plt.figure(figsize = (10,10))
sn.heatmap(con_mat, annot=True)
plt.xlabel("Predicted")
plt.ylabel("True or False")
plt.show()
