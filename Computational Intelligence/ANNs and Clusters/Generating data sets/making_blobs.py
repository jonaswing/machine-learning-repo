from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate 500 samples across 6 different blobs.
# The cluster centers have a standard deviation of 1.2.
# random_state is set to 100 to ensure reproducibility.
blob_X, blob_y = make_blobs(n_samples = 500,
                       centers = 6,
                       cluster_std = 1.2,
                       random_state=100)


# Plot the blobs
plt.figure(figsize=(8, 6))
plt.scatter(blob_X[:, 0], blob_X[:, 1], c=blob_y, cmap='viridis', s=50, alpha=0.7)
plt.title('Blobs')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster')
plt.show()

