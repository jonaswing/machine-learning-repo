import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs, make_moons, make_circles
from matplotlib import pyplot as plt


x1, y1 = make_blobs()

x2, y2 = make_moons()

x3, y3 = make_circles()


fig, ax = plt.subplots(3, sharex=True)

# Create a scatter plot using the default colormap of "viridis".
# The color values are taken from the x-coordinates of the plot.
ax[0].scatter(x1[:, 0], x1[:, 1], c=x1[:, 0])
# Create a scatter plot using the "rainbow" colormap.
# The color values are taken from the x-coordinates of the plot.
ax[1].scatter(x2[:, 0], x2[:, 1], c=x2[:, 0], cmap="rainbow")
# Create a scatter plot using the "Paired" colormap.
# The color values are taken from the y-coordinates of the plot.
ax[2].scatter(x3[:, 0], x3[:, 1], c=x3[:, 1], cmap="Paired")


plt.show()


