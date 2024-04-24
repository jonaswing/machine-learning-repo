# import numpy under the alias np and
# pandas under the alias pd
import numpy as np
import pandas as pd
# import train_test_split from the scikit-learn.model_selection module
from sklearn.model_selection import train_test_split

# Generate a data set containing 500 random integers in the range 0 to 1000
# across 2 columns as the independent (input) variables
X = np.random.randint(1000, size=(250,2))
# Generate a data set containing 250 random integers in the range 0 to 3
# across 1 columns as the dependent (output) variables
y = np.random.randint(3, size=(250,1))

# Generate training and test sets for both the input and output variable.  The function
# assumes that data sets X and y are parallel (related) and splits them as such.
# The test_size of .2 results in an 80/20 split and the random_state of 1 (could have been any int)
# ensures that the splitting happens the same every time.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=1)

# Print out the shape of each data set
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)