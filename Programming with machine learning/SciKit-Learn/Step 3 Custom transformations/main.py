# import numpy under the alias np and
# pandas under the alias pd
import numpy as np
import pandas as pd
# import FunctionTransformer from the scikit-learn.preprocessing module
from sklearn.preprocessing import FunctionTransformer

# The first parameter X is an array and
# the second is the threshold with a default of 0.0
def MyBinarizer(X, threshold=0.0):
    # Change all values above the threshold to 1 and the rest to 0
    # returns the modified Numpy array
    return np.where(X > threshold, 1, 0)

# Generate a data set containing 250 random integers in the range 0 to 1000
# in a single column.
data = np.random.randint(1000, size=(250,1))
demo = pd.DataFrame(data, columns=["Feature 1"])

# Create a FunctionTransformer which calls the function MyBinarizer.
# The array is passed to the first parameter of the function (X)
# kw_args receives a sequence of key-value pairs to assign values to any other
# function parameters.
binary = FunctionTransformer(func=MyBinarizer,kw_args={"threshold":350})
demo["Feature 1_binary"] = binary.transform(demo["Feature 1"].values.reshape(-1,1))
# Display the first 10 rows of the data set
print(demo.head(10))