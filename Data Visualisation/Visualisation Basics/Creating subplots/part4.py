from matplotlib import pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 11, 4, 9]
x2 = [1, 2, 3, 4, 5]
y2 = [7, 15, 20, 25, 30]
x3 = [-5, -4, 1, 20, 35]
y3 = [-22, -9, 2, 8, 17]
x4 = [0.2, 0.45, 0.79, 0.87, 0.96]
y4 = [1, 2, 3, 3, 5]

# Create 4 sub-plots which share a y-axis per row
# and an x-axis across all plots.
fig, axs = plt.subplots(4, sharex=True, sharey="row")
# Remove the horizontally spanning space between the sub-plots.
fig.subplots_adjust(hspace=0)
# Plot a line on the first Axis.
axs[0].plot(x1, y1)
# Plot a line on the second Axis.
axs[1].plot(x1, y1)
# Plot a line on the third Axis.
axs[2].plot(x1, y1)
# Plot a line on the fourth Axis.
axs[3].plot(x1, y1)
plt.show()