import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)


# Define the range for the heatmap
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

# Create a grid of points
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# Use a colormap other than the default
cmap = plt.cm.coolwarm

# Generate heatmap
plt.figure(figsize=(8, 6))
plt.imshow(np.flipud(np.random.rand(len(xx), len(yy))), cmap=cmap, extent=(x_min, x_max, y_min, y_max))
plt.colorbar(label='Density')
plt.scatter(X[:, 0], X[:, 1], s=30, edgecolors='k')
plt.title('Heatmap of Data Density')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid(True)
plt.show()








