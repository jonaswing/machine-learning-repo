# Import numpy and LinearRegression from sklearn.linear_model
import numpy as np
from sklearn.linear_model import LinearRegression


# Load data from a file.
data = np.loadtxt("FranchiseFeeVSStartUpCost.csv", delimiter=";", dtype=np.float64)
# Output the first 5 rows from the data set.
print("First 5 rows of data:\n",  data[0:5, :])

# Declare training data
# Select the first column from the data set as the input feature.
# The column is converted to a multi-dimensional array.
x = data[:, 0].reshape(-1,1 )
# Select the second column from the data set as the output feature.
y = data[:, 1]


# Create a new LinearRegression object.
model = LinearRegression()
# Train the model.
model.fit(x, y)
# Output the model intercept and slope.
print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)

# Use the model to generate predictions.
y_pred = model.predict(x)
# Output the first 10 predictions.
print("\nFirst 10 x, y and predicted y values:")
print("{0:6}\t{1:6}\t{2:6}".format("x","y","y_pred"))
for i in range(0, 10):
    print("{0:6}\t{1:6}\t{2:6.1f}".format(x[i,0], y[i], y_pred[i]))
