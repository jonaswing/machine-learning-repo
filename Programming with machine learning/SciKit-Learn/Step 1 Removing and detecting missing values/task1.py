import pandas as pd
import numpy as np
from sklearn.impute import MissingIndicator


data = np.random.randint(0, 501, size=(10, 4)).astype(float)

# Replace some values with 777
replace_with_777 = np.random.choice([True, False], size=(10, 4), p=[0.1, 0.9])
data[replace_with_777] = 777

# Replace some values with np.NaN
replace_with_nan = np.random.choice([True, False], size=(10, 4), p=[0.1, 0.9])
data[replace_with_nan] = np.NaN

# Create a DataFrame using Pandas
data = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

print(data, "\n")


data.replace({777: np.NaN}, inplace=True)

print(data, "\n")


# Declare a new MissingIndicator
mi = MissingIndicator(missing_values=np.NaN)

# Apply the transformation to the data DataFrame
mi = mi.fit_transform(data)

# Create a new DataFrame containing the generated features
mi = pd.DataFrame(mi, columns=['m1', 'm2', 'm3', 'm4'])

print(mi, "\n")

