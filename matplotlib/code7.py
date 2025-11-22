# plotting three variables
import numpy as np
import matplotlib.pyplot as plt

data1 = [12,34,35,56,76]
data2 = [15,46,63,21,43]
data3 = [35,10,43,67,90]

plt.plot(data1, label = "company1")
plt.plot(data2, label = "company2")
plt.plot(data3, label = "company3")
plt.legend(loc = "upper left")
plt.plot(data2)
plt.plot(data3)
plt.show()