# box plot
import numpy as np
import matplotlib.pyplot as plt

heights = np.random.normal(50,10,1000)
print(heights)

plt.boxplot(heights)
plt.show()