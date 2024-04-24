from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

# Generate 500 samples with 0.1 standard deviation for the noise.
# Random_state is set to 100 to ensure reproducibility.
# Factor is set to 0.5 to increase the distance between the circles.
circle_X, circle_y  = make_circles(n_samples=500,
                                   noise=0.1,
                                   random_state=100,
                                   factor=0.5)


# Plot the blobs
plt.figure(figsize=(8, 6))
plt.scatter(circle_X[:, 0], circle_X[:, 1], c=circle_y, cmap='viridis', s=50, alpha=0.7)
plt.title('Blobs')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster')
plt.show()
