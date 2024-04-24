# Import numpy and LinearRegression from sklearn.linear_model
import numpy as np
from sklearn.linear_model import LinearRegression
# Import pickle and os
import pickle
import os

# Declare training data
# Input data (x) should be a multi-dimensional array.  In this case
# a single input feature (1 column) with multiple rows of data.
x = np.array([3, 12, 23, 38, 44, 54, 66, 74, 86, 94]).reshape((-1, 1))
# Output data (y) / dependent variables.  The number of rows
# in the output data should match the number of rows in the input data.
y = np.array([3, 22, 18, 31, 55, 41, 37, 67, 66, 82])


# Test whether the pickle exists.
if os.path.isfile("linear_regression.mdl"):
    # If the pickle exists, open it.
    infile = open("linear_regression.mdl",'rb')
    # Load the pickle.
    model = pickle.load(infile)
    # Close the pickle file.
    infile.close()
    # Output a message to state that the pickle was
    # successfully loaded.
    print("Loaded pickle")
else:
    # Create a new LinearRegression object.
    model = LinearRegression()
    # Train the model.
    model.fit(x, y)
    # Open a file to save the pickle.
    outfile = open("linear_regression.mdl","wb")
    # Store the model in the file.
    pickle.dump(model, outfile)
    # Close the pickle file.
    outfile.close()


# Declare test data
x_test = np.array([7, 10, 15, 78, 12]).reshape((-1, 1))

# Use the model to generate predictions.
y_pred_test = model.predict(x_test)

# Output the x values and their associated predictions.
print("x\tPredicted y")
for x, y in zip(x_test[:, 0], y_pred_test):
    print("{0}\t{1}".format(x, y))