# import the sklearn datasets and pandas
from sklearn import datasets
import pandas as pd
# Imports the StandardScaler and PCA
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Loads the iris dataset
data, target = datasets.load_iris(return_X_y=True)
# Load the data into a DataFrame
data = pd.DataFrame(data)
# Display the details of the DataFrame
print("Original data:\n", data.head())
# Standardise the data with the StandardScaler
data = StandardScaler().fit_transform(data)
# Load the data into a DataFrame
data = pd.DataFrame(data)
# Display the details of the standardised DataFrame
print("\nStandardised data:\n", data.head())

# Create a PCA object to reduce the number of components (features)
# to 2.
pca = PCA(n_components=2)
# Use the PCA object to reduce the number of features to 2
data = pca.fit_transform(data)
# Load the data into a DataFrame
data = pd.DataFrame(data)
# Display the details of the standardised DataFrame
print("\nReduced features data:\n", data.head())