# Import pyplot from matplotlib as plt.
from matplotlib import pyplot as plt

# Request a Figure (fig) and Axes (ax) object
# using subplots().
fig, ax = plt.subplots()
# Define the x and y coordinates.
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 11, 4, 9]
x2 = [1, 2, 3, 4, 5]
y2 = [7, 15, 20, 25, 30]
# Draw a line using the x and y coordinates.
# ax.plot(x, y)
# Draw a styled line using the x and y coordinates.
ax.plot(x1, y1, color="green", linewidth=5, linestyle="dashed")
ax.plot(x2, y2, c="blue", lw=2, ls="-.")
# Display the plotted figure.
plt.show()