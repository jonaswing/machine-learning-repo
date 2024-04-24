# Import pyplot from matplotlib as plt.
from matplotlib import pyplot as plt

# Request a Figure (fig) and Axes (ax) object
# using subplots().
fig, ax = plt.subplots()
# Define the x and y coordinates.
x = [1, 2, 3, 4, 5]
y = [2, 4, 11, 4, 9]

# Draw a line using the x and y coordinates.
# ax.plot(x, y)
# Draw a styled line using the x and y coordinates.
ax.plot(x, y, color="green", linewidth=5, linestyle="dashed")
ax.set_title("A simple plot")
ax.set_xlabel("The details for the x-axis")
ax.set_ylabel("The details for the y-axis")
# Previous statements to plot the figure and labels

ax.text(3.2, 10.5, "The first annotation")
ax.text(1.3, 2, "The second annotation", c="white", backgroundcolor="red", fontsize=22)

# Display the plotted figure.
plt.show()