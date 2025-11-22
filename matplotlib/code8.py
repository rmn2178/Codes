# 3d plotting
import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection = "3d")

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

ax.scatter(x,y,z,c = "red")
ax.set_title("Scatter Plot 3D")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
plt.show()