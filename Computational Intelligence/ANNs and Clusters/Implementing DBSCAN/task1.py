from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans


# Make blobs
X, y = make_blobs(n_samples=1000, centers=5, n_features=8)


# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


# Train model
model = KMeans(n_clusters=2)

model.fit(X_train, y_train)




