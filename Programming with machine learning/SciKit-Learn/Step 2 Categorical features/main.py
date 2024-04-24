# import numpy under the alias np and
# pandas under the alias pd
import numpy as np
import pandas as pd
# import OrdinalEncoder, OneHotEncoder and LabelEncoder from the scikit-learn.preprocessing module
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder


# Declare an input data set using a list.
data = [['Y', 'Oslo', '18 to 35'],
        ['N', 'Bergen', 'Under 18'],
        ['N','Kristiansand', '36 to 65'],
        ['Y','Kristiansand','Over 65'],
        ['N', 'Oslo', 'Under 18']]

# Create a Pandas DataFrame from the data
demo = pd.DataFrame(data, columns=['loyalty', 'city', 'age_group'])
# Display the contents of the DataFrame
print(demo, "\n")


# Create a new OrdinalEncoder
# Specifies the sequence in which values should be allocated by the encoder
# if not specified, the values may be assigned in a manner which may not make sense,
# e.g. Under 18 could be 3 and 36 to 65 could be 0.  By providing the categories
# the values are forced so that Under 18 is 0, 18 to 35 is 1, etc.
# If the dtype is not set to int, values may be assigned as float.
encoder = OrdinalEncoder(dtype=int, categories=[['Under 18', '18 to 35', '36 to 65', 'Over 65']])
# Uses the encoder to only encode the values of the age_group column.
# The resulting numpy array is reshaped to contain 1 column and the number of rows
# is derived from the number of elements in the array (specified by -1).
# The encoded column is assigned over the original age_group column.
demo.age_group = encoder.fit_transform(demo.age_group.values.reshape(-1,1))
# Display the contents of the DataFrame
print(demo, "\n")


# Create a new OneHotEncoder to encode values as integers.
# Setting sparse to True creates a sparse array of values.
# Setting it to False does not create a sparse array.
onehot = OneHotEncoder(dtype=int, sparse_output=True)
# Create a new DataFrame to store the one hot encoded data
# for columns loyalty and city with the predefined
# alphabetical column names.
final = pd.DataFrame(
    onehot.fit_transform(demo[['loyalty', 'city']]).toarray(),
    columns=['N', 'Y', 'Bergen', 'Kristiansand','Oslo'])
# Add the results from the OrdinalEncoder as an extra column to
# the DataFrame.
final['age_group'] = demo.age_group
# Display the contents of the DataFrame
print(final, "\n")


# Create a LabelEncoder and set it up to fit for the values Y and N
labels_loyalty = LabelEncoder()
labels_loyalty.fit(["Y", "N"])
# Use the labels_loyalty encoder to encode the loyalty column of demo
demo.loyalty = labels_loyalty.transform(demo.loyalty.values.ravel())
# Create a LabelEncoder and set it up to fit for the values Bergen, Kristiansand and Oslo
labels_city = LabelEncoder()
labels_city.fit(["Bergen", "Kristiansand", "Oslo"])
# Use the labels_city encoder to encode the city column of demo
demo.city = labels_city.transform(demo.city.values.ravel())
# Display the contents of the DataFrame
print(demo)