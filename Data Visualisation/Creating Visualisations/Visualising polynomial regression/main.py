# Import numpy and LinearRegression from sklearn.linear_model
import numpy as np
from sklearn.linear_model import LinearRegression
# Import PolynomialFeatures from sklearn.preprocessing
from sklearn.preprocessing import PolynomialFeatures
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Declare training data
# Input data (x) should be a multi-dimensional array. In this case
# a single input feature (1 column) with multiple rows of data.
# The data consists of 10 values spaced equally from 1 to 100.
x = np.linspace(1, 100, 10).reshape((-1, 1))
# Output data (y) / dependent variables. The number of rows
# in the output data should match the number of rows in the input data.
y = np.array([20, 34, 46, 10, 15, 17, 46, 66, 77, 82])

# Train a "normal" linear regression model and
# make predictions.
model_lin = LinearRegression()
model_lin.fit(x, y)
normal_y_pred = model_lin.predict(x)

# Plot the data points as a scatter plot.
plt.scatter(x, y, color="blue")
# Draw the linear regression line.
plt.plot(x, normal_y_pred, color="green", linewidth=2, linestyle="dashed")


# Create a new PolynomialFeatures object.
transformer = PolynomialFeatures(degree=2, include_bias=False)
# Use it to transform the x values.
x_trans = transformer.fit_transform(x)
# Create a new LinearRegression object.
model = LinearRegression()
# Train the model.
model.fit(x_trans, y)


# Find the minimum and maximum values of the first column of the
# transformed features.
min_value = np.min(x_trans[:, 0])
max_value = np.max(x_trans[:, 0])

# Generate a sequence of 100 values for the x-axis. These values are in
# range from the minimum to the maximum for the first transformed feature.
X_seq = np.linspace(min_value, max_value, 100).reshape(-1,1)
# Create transformed versions of the generated x-coordinates.
X_seq_trans = transformer.transform(X_seq)
# Generate predictions for the transformed x-coordinates.
y_pred = model.predict(X_seq_trans)


# Draw the polynomial regression line using the sequential x-coordinates
# and predicted y-coordinates..
plt.plot(X_seq, y_pred, color="red", linewidth=2)
# Display the Figure.
plt.show()

