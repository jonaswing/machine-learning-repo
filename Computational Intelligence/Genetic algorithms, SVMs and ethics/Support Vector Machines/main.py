from sklearn import datasets

#Load the dataset.
data = datasets.load_breast_cancer()
# Display the names of the dataset's features.
print("Features:\n", data.feature_names)
# Display the names of the labels.
print("Labels: ", data.target_names)
# Display the shape of the dataset.
print("Shape: ", data.data.shape)
# Display the first record from the dataset.
print("First record:\n", data.data[0])


