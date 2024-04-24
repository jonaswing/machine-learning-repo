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
# Elements containing a "." will be left empty.
fig, axd = plt.subplot_mosaic([["A", "."],
                               [".", "B"]])


# When using subplot_mosaic(), the subplot structure may also be
# specified as a string instead of a List. For instance,
# the above subplot could’ve been structured as follows:
# fig, axd = plt.subplot_mosaic('''
#                                A.
#                                .B
#                               ''')


# Plot the various lines. The Axis objects are
# accessed using the keys defined in the subplot_mosaic
# call. The plots will span the Figure as specified
# in the list structure/contents.
axd["A"].plot(x1, y1)
axd["B"].plot(x2, y2)
plt.show()

