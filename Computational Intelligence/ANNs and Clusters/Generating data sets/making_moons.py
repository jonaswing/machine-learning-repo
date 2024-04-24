from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

# Generate 500 samples with 0.1 standard deviation for the noise.
# Random_state is set to 100 to ensure reproducibility.
moon_X, moon_y  = make_moons(n_samples=500,
                             noise=0.1,
                             random_state=100)


# Plot the blobs
plt.figure(figsize=(8, 6))
plt.scatter(moon_X[:, 0], moon_X[:, 1], c=moon_y, cmap='viridis', s=50, alpha=0.7)
plt.title('Blobs')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster')
plt.show()

