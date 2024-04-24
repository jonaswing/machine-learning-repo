import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_circles


X, y = make_circles(n_samples=250, noise=0.1)

# Define a DBSCAN object with an eps of 1.5 and min_samples of 2
model = DBSCAN(eps=1.5, min_samples=2)
# Run the clustering algorithm on the provided data.
model.fit(X)

# Create a set of unique labels.
clusters = set(model.labels_)
# Test if a label of -1 is included and remove it.
# -1 is an indicator of noise and not representative of a cluster.
if -1 in clusters:
    clusters.remove(-1)
# Output the number of clusters.
print("Clusters found: {0}\n".format(len(clusters)))


# Create a DataFrame of the input data and the generated labels.
df = pd.DataFrame({"X1":X[:,0],"X2":X[:,1], "y":model.labels_})
print(df.head())