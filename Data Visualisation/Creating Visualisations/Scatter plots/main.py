from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs

# Generate 500 data points. random_state is set
# to 12 to ensure reproducibility.
X, y = make_blobs(n_samples=500,
                  centers=1,
                  n_features=2,
                  random_state=12,
                  cluster_std=1.5)

fig, ax = plt.subplots(2,)
# Plot a simple scatter plot using the data generated using make_blobs().
ax[0].scatter(X[:,0], X[:,1])
# Plot the same data, but using diamond-shaped green markers with purple edges.
# The markers are drawn at an increased size and half-opaque.
ax[1].scatter(X[:,0], X[:,1], marker="D",
              s=200, c="green",
              edgecolor="purple", alpha=0.5)
plt.show()