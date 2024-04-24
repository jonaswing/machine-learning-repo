from matplotlib import pyplot as plt

# Define the data for the plots.
x1 = [1 , 9]
y1 = [1,  7]
x2 = [1, 4, 5, 7, 9]
y2 = [2, 5, 3, 11, 4]

# Create the two line plots and show the figure.
plt.plot(x1, y1)
plt.plot(x2, y2, "8--m")
plt.show()