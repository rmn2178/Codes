# line plot
import matplotlib.pyplot as plt

number = [x for x in range(1,30)]
square = [x*x for x in range(1,30)]

print(number)
print(square)

# c is the color
# lw is the thickness
# linestyle is the style of the line
plt.plot(number,square,c='r', lw = 3 , linestyle = '--')
plt.title("Square Number")
plt.xlabel("Square Number")
plt.ylabel("Number")
plt.show()