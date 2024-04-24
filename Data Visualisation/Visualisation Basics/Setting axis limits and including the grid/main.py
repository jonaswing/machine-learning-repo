from matplotlib import pyplot as plt
# Request a Figure (fig) and Axes (ax) object
# using subplots().
fig, ax = plt.subplots()
# Define the x and y coordinates.
x = [50, 78, 93, 112, 134, 178]
y = [78, 73, 82, 89, 100, 145]
# Draw a styled line using the x and y coordinates.
ax.plot(x, y, color="purple", linewidth=5, linestyle="-.")
ax.axis([40, 190, 40, 190])
ax.grid(True)
# Display the plotted figure.
plt.show()