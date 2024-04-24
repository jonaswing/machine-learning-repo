from matplotlib import pyplot as plt
# Request a Figure (fig) and Axes (ax) object
# using subplots().
fig, ax = plt.subplots()
# Define the x and y coordinates.
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 11, 4, 9]
x2 = [1, 2, 3, 4, 5]
y2 = [7, 15, 20, 25, 30]
# Draw line graphs and display the default legend.
ax.plot(x1, y1, color="green", linewidth=5, linestyle="dashed", label="Line 1")
ax.plot(x2, y2, c="blue", lw=2, ls="-.", label="Line 2")
ax.legend()
plt.show()