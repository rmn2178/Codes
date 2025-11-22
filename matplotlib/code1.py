# scatter plot
import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(100)*100
y_data = np.random.random(100)*100

# c = color
# marker is the marking symbol
# s is the size of the marker
# alpha is the transparency
plt.scatter(x_data, y_data ,c = "#000" ,marker = "o",s = 40 ,alpha = 0.5 )
plt.show()