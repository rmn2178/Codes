import numpy as np
import matplotlib.pyplot as plt

# Input data
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([3, 4, 6, 8, 9, 11])

# Initialize parameters
m = 0
b = 0
epochs = 1000
learning_rate = 0.01
n = len(x)
cost_history = []

# Gradient Descent
for i in range(epochs):
    y_pred = m * x + b
    error = y - y_pred
    cost = (1/n) * sum(error ** 2)
    cost_history.append(cost)

    # Gradients
    m_grad = -(2/n) * sum(x * error)
    b_grad = -(2/n) * sum(error)

    # Update parameters
    m -= learning_rate * m_grad
    b -= learning_rate * b_grad

    if i % 100 == 0:
        print(f"Epoch {i}: m={m:.4f}, b={b:.4f}, cost={cost:.4f}")

# Final model
print(f"\nFinal equation: y = {m:.2f}x + {b:.2f}")

# Plot cost vs iterations
plt.plot(range(epochs), cost_history)
plt.title("Cost vs Iterations")
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.grid(True)
plt.show()