# histogram
import numpy as np
import matplotlib.pyplot as plt

ages = np.random.normal(20,1.5,1000)

print(ages)

# bins is the number of hists
# color is the color of the hist
# edgecolor is the border color
# line width is the width of the border
plt.hist(ages,
         bins=[ages.min(),18,21,ages.max()],
         color="red",
         edgecolor="black",
         linewidth=2)
plt.show()