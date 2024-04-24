import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_circles


X, y = make_circles(n_samples=250, noise=0.1)

# Define a KMeans object to create 6 clusters.
model = KMeans(n_clusters=6)
# Run the clustering algorithm on the provided data.
model.fit(X)
# Output the model centroids
print("Centroids:\n", model.cluster_centers_)


# Create a DataFrame of the input data and the generated labels.
df = pd.DataFrame({"X1":X[:,0],"X2":X[:,1], "y":model.labels_})
print(df.head())


# Create three test data entries consisting of new data.
test_data = [[1.34, 4.23], [3.22, 1.42], [-2.4, 8.7]]
# Predict which cluster these samples belong to.
pred = model.predict(test_data)
# Output the result
print(pred)

