import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_circles

# Generate data
X, y = make_circles(n_samples=250, noise=0.1)

# Define a DBSCAN object with an eps of 0.2 and min_samples of 5
model = DBSCAN(eps=0.2, min_samples=5)
# Run the clustering algorithm on the provided data.
model.fit(X)

# Create a DataFrame of the input data and the generated labels.
df = pd.DataFrame({"X1": X[:, 0], "X2": X[:, 1], "y": model.labels_})

# Plot the clusters
plt.figure(figsize=(8, 6))

# Plot points for each cluster
unique_labels = set(model.labels_)
for label in unique_labels:
    if label == -1:
        # Plot noise points as black
        noise_mask = (model.labels_ == label)
        plt.scatter(X[noise_mask, 0], X[noise_mask, 1], c='black', marker='x', label='Noise')
    else:
        # Plot points for each cluster
        cluster_mask = (model.labels_ == label)
        plt.scatter(X[cluster_mask, 0], X[cluster_mask, 1], label=f'Cluster {label}')

plt.title('DBSCAN Clustering')
plt.xlabel('X1')
plt.ylabel('X2')
plt.legend()
plt.show()
