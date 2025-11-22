# Histogram
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
# kde is the flow line if true
# shows the relation of the value
sns.histplot(tips['tip'],kde=True)
plt.show()

# barplot
# it gives the relation between the divisions of the data
sns.barplot(x="sex", y="tip",data = tips, palette="YlGnBu")
plt.show()

# boxplot
# it gives the boxplot
sns.boxplot(x="day", y="tip", data=tips, palette="YlGnBu")
plt.show()

# strip-plot
# It makes the data to be strip plotted
sns.stripplot(x=tips['day'], y=tips['total_bill'], data=tips ,hue = "sex" ,palette="YlGnBu", dodge=True)
plt.show()
