import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generate data
X, _ = make_blobs(n_samples=350, n_features=3, centers=5, random_state=42)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for label in set(labels):
    ax.scatter(X[labels == label][:, 0], X[labels == label][:, 1], X[labels == label][:, 2], label=f'Cluster {label + 1}')

ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], c='black', marker='o', s=100, label='Centroids')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Cluster Plot')
ax.legend()

plt.savefig('3D_cluster_plot.jpg')
plt.show()
