import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_circles

# Generate sample data
X, _ = make_circles(n_samples=250, noise=0.1)

# Define a KMeans object to create 6 clusters.
model = KMeans(n_clusters=6, random_state=42)
# Run the clustering algorithm on the provided data.
model.fit(X)
# Output the model centroids
print("Centroids:\n", model.cluster_centers_)

# Create a DataFrame of the input data and the generated labels.
df = pd.DataFrame({"X1": X[:, 0], "X2": X[:, 1], "y": model.labels_})
print(df.head())


# Plot clusters and centroids
plt.figure(figsize=(8, 6))

# Plot data points
plt.scatter(X[:, 0], X[:, 1], c=model.labels_, cmap='viridis', s=50, alpha=0.5, label='Data Points')

# Plot centroids
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], marker='x', s=200, c='red', label='Centroids')


plt.xlabel('X1')
plt.ylabel('X2')
plt.title('KMeans Clustering with Centroids and Test Data')
plt.legend()
plt.grid(True)
plt.show()
