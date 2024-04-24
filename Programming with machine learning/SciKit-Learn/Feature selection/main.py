# import the sklearn datasets
from sklearn import datasets
# Imports the SelectKBest selector as well as the chi2 object
# (required by the SelectKBest selector)
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
# Loads the digits dataset
data, target = datasets.load_digits(return_X_y=True)
# Display the shape of the digits data set's data attribute
print("Initial shape: ", data.shape)
# Creates a SelectBest object to select the 5 best performing features
selector = SelectKBest(chi2, k=20)
# Passes both the data and target to the selector's fit_transform method.
# To test the performance of the data features, the target is necessary.
data_new = selector.fit_transform(data, target)
# Display the shape of the diabetes data set's revised data structure
# after feature selection.
print("Revised shape: ", data_new.shape)