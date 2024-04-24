import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons, make_circles
from matplotlib.colors import ListedColormap

# Generate three different datasets
data_blobs, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)
data_moons, _ = make_moons(n_samples=300, noise=0.1, random_state=42)
data_circles, _ = make_circles(n_samples=300, factor=0.5, noise=0.1, random_state=42)

# Create a figure with sub-plots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plot for make_blobs()
cmap_blobs = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF', '#FFFFAA'])
scatter_blobs = axes[0].scatter(data_blobs[:, 0], data_blobs[:, 1], c=data_blobs[:, 1], cmap=cmap_blobs, marker='o')
axes[0].set_title('make_blobs')
fig.colorbar(scatter_blobs, ax=axes[0])

# Plot for make_moons()
cmap_moons = ListedColormap(['#FFAAAA', '#AAAAFF'])
scatter_moons = axes[1].scatter(data_moons[:, 0], data_moons[:, 1], c=data_moons[:, 1], cmap=cmap_moons, marker='x')
axes[1].set_title('make_moons')
fig.colorbar(scatter_moons, ax=axes[1])

# Plot for make_circles()
cmap_circles = ListedColormap(['#FFAAAA', '#AAAAFF'])
scatter_circles = axes[2].scatter(data_circles[:, 0], data_circles[:, 1], c=data_circles[:, 1], cmap=cmap_circles, marker='^')
axes[2].set_title('make_circles')
fig.colorbar(scatter_circles, ax=axes[2])

plt.tight_layout()
plt.show()
