from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Load the CSV file
df = pd.read_csv('bike_sell_data.csv')

# Split the entire DataFrame (all three columns)
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Print sizes
print("Training set size:", len(train_df))
print("Testing set size:", len(test_df))

# Separate features and target
X_train = train_df[['run', 'age']]
y_train = train_df['price']
X_test = test_df[['run', 'age']]
y_test = test_df['price']

# Create and train the model
clf = LinearRegression()
clf.fit(X_train, y_train)

# Print model coefficients
print("\nModel Coefficients:")
print("Intercept:", clf.intercept_)
print("Coefficients:", clf.coef_)

# Predict on test set
y_pred = clf.predict(X_test)

# Compare predictions with actual values
results = pd.DataFrame({
    'Actual Price': y_test.values,
    'Predicted Price': y_pred
})
print("\nPrediction Results:\n", results)

# To print the accuracy
accuracy = clf.score(X_test, y_test)
print("\nAccuracy:", accuracy)