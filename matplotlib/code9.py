# 3d plotting
import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection = "3d")

x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)

X,Y = np.meshgrid(x,y)
Z = np.sin(X) * np.cos(Y)
ax.plot_surface(X,Y,Z)

ax.set_title("Scatter Plot 3D")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
plt.show()