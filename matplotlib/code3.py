# bar plot
import matplotlib.pyplot as plt

letter = ["a","b","c","d","e","f","g","h","i"]
number = [20,50,30,100,30,70,10,50,100]

# color is the color of the bar
# align is the alignment of the word below the bar
# width is the width of the bar
# edgecolor is the marking of the border
# lw is the thickness of the border
plt.bar(letter,number,color="red",align = "edge",width=0.3,edgecolor="black",lw = 3)
plt.show()