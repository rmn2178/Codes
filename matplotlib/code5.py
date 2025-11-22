# pie chart
import matplotlib.pyplot as plt

language = ['c','c++','java','javascript','python','golang']
popularity = [10,14,25,34,78,32]

# explode slightly takes out the pie
plt.pie(popularity,labels = language,
        explode = (0.1,0,0,0,0.04,0),
        autopct="%.2f%%",       # decimal value percentage
        pctdistance = 3,        # distance to show
        shadow = True,          # shadow forms
        startangle = 90)        # angle to slide
plt.show()