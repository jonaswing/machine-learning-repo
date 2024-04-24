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


# Remove all rows (axis=0), where at least one value is not NaN (thresh=1)
# and apply the changes directly to the dataset (inplace=True)
demo.dropna(axis=0, thresh=1, inplace=True)
# Display the contents of the DataFrame
print(demo, "\n")


# Recalculate the index of the DataFrame
demo.reset_index(inplace=True)
# Drop the original index column
demo.drop(['index'], axis=1, inplace=True)
# Display the contents of the DataFrame
print(demo, "\n")


# Replace all 999 values with NaN
demo.replace({999 : np.NaN}, inplace=True)
# Display the contents of the DataFrame
print(demo, "\n")


# Declare a new MissingIndicator
mi = MissingIndicator(missing_values=np.NaN)
# Apply the transformation to the demo DataFrame
mi = mi.fit_transform(demo)
# Create a new DataFrame containing the generated features
mi = pd.DataFrame(mi, columns=['m1', 'm3'])
# Display the contents of the new DataFrame
print(mi, "\n")