from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs

# Generate 500 data points. random_state is set
# to 12 to ensure reproducibility.
X, y = make_blobs(n_samples=500,
                  centers=1,
                  n_features=2,
                  random_state=12,
                  cluster_std=1.5)


fig, ax = plt.subplots(2, 2)
# Create a scatter plot using the default colormap of "viridis".
# The color values are taken from the x-coordinates of the plot.
ax[0, 0].scatter(X[:, 0], X[:, 1], c=X[:, 0])
# Create a scatter plot using the "rainbow" colormap.
# The color values are taken from the x-coordinates of the plot.
ax[0, 1].scatter(X[:, 0], X[:, 1], c=X[:, 0], cmap="rainbow")
# Create a scatter plot using the "Paired" colormap.
# The color values are taken from the y-coordinates of the plot.
ax[1, 0].scatter(X[:, 0], X[:, 1], c=X[:, 1], cmap="Paired")
# Create a scatter plot using the "hsv" colormap.
# The color values are taken from the y-coordinates of the plot.
# A ScalarMappable object is returned from the scatter plot and
# stored as plot4.
plot4 = ax[1, 1].scatter(X[:, 0], X[:, 1], c=X[:, 1], cmap="hsv")
# Applies a colormap using the ScalarMappable object associated with
# the plot at ax[1, 1]. Since the ax and cax parameters are not
# defined, the colorbar is added to the plot directly.
fig.colorbar(plot4)
plt.show()