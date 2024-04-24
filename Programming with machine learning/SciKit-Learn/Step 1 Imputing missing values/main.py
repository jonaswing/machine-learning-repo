# import numpy under the alias np and
# pandas under the alias pd
import numpy as np
import pandas as pd
# import MissingIndicator from the scikit-learn.impute module
from sklearn.impute import MissingIndicator
# import SimpleImputer from the scikit-learn.impute module
from sklearn.impute import SimpleImputer


# Declare an input data set using a list.
data = [[55, 78, 34],
        [np.NaN, np.NaN, np.NaN],
        [-24,5,13],
        [999,0.5,-0.5],
        [np.NaN, 0, np.NaN]]

# Create a Pandas DataFrame from the data
demo = pd.DataFrame(data)
# Assign column names to the DataFrame
demo.columns = ['Feature 1', 'Feature 2', 'Feature 3']
# Display the contents of the DataFrame
print(demo, "\n")


# Create a SimpleImputer to replace al NaN with the mean
with_mean = SimpleImputer(missing_values=np.NaN, strategy="mean")
# Applies the transformation and generates a numpy array of the data set
with_mean = with_mean.fit_transform(data)
# Use the numpy array to create a new DataFrame
with_mean = pd.DataFrame(with_mean, columns=("Feature 1", "Feature 2", "Feature 3"))
# Output the DataFrame with the missing values replaced with the mean
print("Replaced with mean:\n", with_mean, "\n")


# Create a SimpleImputer to replace al NaN with the median
with_median = SimpleImputer(missing_values=np.NaN, strategy="median")
# Applies the transformation and generates a numpy array of the data set
with_median = with_median.fit_transform(demo)
# Use the numpy array to create a new DataFrame
with_median = pd.DataFrame(with_median, columns=("Feature 1", "Feature 2", "Feature 3"))
# Output the DataFrame with the missing values replaced with the mean
print("\nReplaced with median:\n", with_median, "\n")


# Create a SimpleImputer to replace al NaN with the most frequent value
with_most_frequent = SimpleImputer(missing_values=np.NaN, strategy="most_frequent")
# Applies the transformation and generates a numpy array of the data set
with_most_frequent = with_most_frequent.fit_transform(demo)
# Use the numpy array to create a new DataFrame
with_most_frequent = pd.DataFrame(with_most_frequent, columns=("Feature 1", "Feature 2", "Feature 3"))
# Output the DataFrame with the missing values replaced with the mean
print("\nReplaced with most_frequent:\n", with_most_frequent, "\n")


# Create a SimpleImputer to replace al NaN with the constant value 10
# as defined using the fill_value parameter
with_constant_10 = SimpleImputer(missing_values=np.NaN, strategy="constant", fill_value=10)
# Applies the transformation and generates a numpy array of the data set
with_constant_10 = with_constant_10.fit_transform(demo)
# Use the numpy array to create a new DataFrame
with_constant_10 = pd.DataFrame(with_constant_10, columns=("Feature 1", "Feature 2", "Feature 3"))
# Output the DataFrame with the missing values replaced with the mean
print("\nReplaced with constant 10:\n", with_constant_10)