# Import pyplot from matplotlib as plt.
from matplotlib import pyplot as plt

# Request a Figure (fig) and Axes (ax) object
# using subplots().
fig, ax = plt.subplots()
# Define the x coordinates.
x = [1, 2, 3, 4, 5]
# Define the y coordinates.
y = [2, 4, 11, 4, 9]
# Draw a line using the x and y coordinates.
ax.plot(x, y)
# Display the plotted figure.
plt.show()