from matplotlib import pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 11, 4, 9]
x2 = [1, 2, 3, 4, 5]
y2 = [7, 15, 20, 25, 30]
x3 = [-5, -4, 1, 20, 35]
y3 = [-22, -9, 2, 8, 17]
x4 = [0.2, 0.45, 0.79, 0.87, 0.96]
y4 = [1, 2, 3, 3, 5]


# Create a single Figure with spanning sub-plots.
# The Axis objects are returned in a dictionary.
fig, axd = plt.subplot_mosaic([["A", "A", "B"],
                               ["A", "A", "B"],
                               ["C", "D", "B"]])

# Plot the various lines. The Axis objects are
# accessed using the keys defined in the subplot_mosaic
# call. The plots will span the Figure as specified
# in the list structure/contents.
axd["A"].plot(x1, y1)
axd["B"].plot(x2, y2)
axd["C"].plot(x3, y3)
axd["D"].plot(x4, y4)
plt.show()