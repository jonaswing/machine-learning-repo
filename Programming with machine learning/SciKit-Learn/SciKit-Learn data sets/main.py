# import the sklearn datasets and pandas
from sklearn import datasets
import pandas as pd
# Output the directory contents of datasets
directories = pd.DataFrame(dir(datasets))
# Display a few details regarding the datasets
print("Number of items:  ", directories.size)
print("\nItems 40 to 50:\n", directories[40:50])


iris_data = pd.DataFrame(datasets.load_iris().data)
iris_data.columns = datasets.load_iris().feature_names
iris_target = pd.DataFrame(datasets.load_iris().target)
iris_target.columns = ["class"]
print("Iris features:\n", iris_data.head())
print("\nIris classes:\n", iris_target.head())
print("\nIris class descriptions:\n", datasets.load_iris().target_names)


# Uses the return_X_y parameter to return the data and target attributes
# as a tuple
data, target = datasets.load_iris(return_X_y=True)
print("data shape: ", data.shape)
print("target shape: ", target.shape)
# Uses the as_frame parameter to return the data as a Pandas DataFrame
# containing all the attributes
iris = datasets.load_iris(as_frame=True)