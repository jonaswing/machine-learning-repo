from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Display the details of the dataset
print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)
print("Number of samples:", len(iris.data))
print("Number of features:", len(iris.feature_names))
print("Data shape:", iris.data.shape)
print("Target shape:", iris.target.shape)
print("Description of the dataset:")
print("OPO", iris.DESCR, "OPO")