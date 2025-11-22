# Scatter plot
import seaborn as sns
from matplotlib import pyplot as plt

# the inbuilt libraries are
# ['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'dowjones', 'exercise', 'flights', 'fmri', 'geyser', 'glue', 'healthexp', 'iris', 'mpg', 'penguins', 'planets', 'seaice', 'taxis', 'tips', 'titanic']

# Loading the tips dataset
tips = sns.load_dataset("tips")
print(tips.head())

#   total_bill   tip     sex smoker  day    time   size
# 0       16.99  1.01  Female   No   Sun   Dinner   2
# 1       10.34  1.66    Male   No   Sun   Dinner   3
# 2       21.01  3.50    Male   No   Sun   Dinner   3
# 3       23.68  3.31    Male   No   Sun   Dinner   2
# 4       24.59  3.61  Female   No   Sun   Dinner   4

# here x and y are the inputs of the graph
# Hue means the color of the dataset
# palette means the color palette off the data points
# size parameter is influenced by the size
# Visualising the tips dataset in seaborn
sns.scatterplot(data=tips, x="total_bill", y="tip",hue = "day", size = "size")
plt.show()