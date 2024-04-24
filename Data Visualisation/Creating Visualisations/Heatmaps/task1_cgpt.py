import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Step 1: Create a dataset with three blobs
X, _ = make_blobs(n_samples=300, centers=3, n_features=2, random_state=42)

# Step 2: Create a heatmap
plt.figure(figsize=(8, 6))
heatmap, xedges, yedges = np.histogram2d(X[:, 0], X[:, 1], bins=50)
plt.imshow(heatmap.T, extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap='viridis')

# Step 3: Plot the dataset values on the heatmap
plt.scatter(X[:, 0], X[:, 1], marker='o', c='red', edgecolor='black')

# Step 4: Add a colorbar
plt.colorbar()
plt.title('Heatmap with Dataset Values')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
