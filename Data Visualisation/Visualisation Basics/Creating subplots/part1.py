import matplotlib.pyplot as plt

# Data for plots
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 11, 4, 9]
x2 = [1, 2, 3, 4, 5]
y2 = [7, 15, 20, 25, 30]
x3 = [-5, -4, 1, 20, 35]
y3 = [-22, -9, 2, 8, 17]
x4 = [0.2, 0.45, 0.79, 0.87, 0.96]
y4 = [1, 2, 3, 3, 5]

# Create a Figure, along with an array of 4 sub-plots (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2)

# Plot lines on each subplot
axs[0, 0].plot(x1, y1)  # Plot a line on the first Axis.
axs[0, 1].plot(x2, y2)  # Plot a line on the second Axis.
axs[1, 0].plot(x3, y3)  # Plot a line on the third Axis.
axs[1, 1].plot(x4, y4)  # Plot a line on the fourth Axis.

# Show the plot
plt.show()
