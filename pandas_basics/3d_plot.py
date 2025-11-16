import matplotlib.pyplot as plt
import pandas as pd

# Load CSV data
df = pd.read_csv('bike_sell_data.csv')

# Create 3D plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(df['run'], df['age'], df['price'], c='red', marker='o')

# Axis labels
ax.set_xlabel('Kilometers Run')
ax.set_ylabel('Age (years)')
ax.set_zlabel('Sell Price (thousands)')
ax.set_title('Bike Data: Run vs Age vs Price')

plt.show()