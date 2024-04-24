from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans


X, y = make_blobs(n_samples=350, n_features=3, centers=5, random_state=42)


kmeans = KMeans(n_clusters=3, random_state=42)


# Fit the model to the data
kmeans.fit(X)

# Get cluster centroids and labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_







