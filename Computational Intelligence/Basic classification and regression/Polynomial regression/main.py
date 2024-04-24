# Import numpy and LinearRegression from sklearn.linear_model
import numpy as np
from sklearn.linear_model import LinearRegression
# Import PolynomialFeatures from sklearn.preprocessing
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# Declare training data
# Input data (x) should be a multi-dimensional array.  In this case
# a single input feature (1 column) with multiple rows of data.
# The data consists of 10 values spaced equally from 1 to 100.
x = np.linspace(1, 100, 10).reshape((-1, 1))
# Output data (y) / dependent variables.  The number of rows
# in the output data should match the number of rows in the input data.
y = np.array([20, 34, 46, 10, 15, 17, 46, 66, 77, 82])


# Create a new PolynomialFeatures object.
transformer = PolynomialFeatures(degree=2, include_bias=False)
# Use it to transform the x values.
x_trans = transformer.fit_transform(x)
# Output the transformed values.
print("Transformed x:\n", x_trans)


# Create a new LinearRegression object.
model = LinearRegression()
# Train the model.
model.fit(x_trans, y)
# Output the model intercept and slope.
print("\nIntercept: ", model.intercept_)
print("Slope: ", model.coef_)
# Use the model to generate predictions.
y_pred = model.predict(x_trans)
# Output the predictions.
print("\n{0:6}\t{1:6}\t{2:6}".format("x","y","y_pred"))
for i in range(0, 10):
    print("{0:6}\t{1:6}\t{2:6.0f}".format(x[i,0], y[i], y_pred[i]))


# Calculate and output the sum of squared errors for the linear regression model.
model_lin = LinearRegression()
model_lin.fit(x, y)
normal_y_pred = model_lin.predict(x)
SSE = sum((y - normal_y_pred) ** 2)
print("Linear SSE:  ", SSE)
# Calculate and output the sum of squared errors for the polynomial regression model.
SSE = sum((y - y_pred) ** 2)
print("Polynomial SSE:  ", SSE)


