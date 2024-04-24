# Import numpy and LinearRegression from sklearn.linear_model
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# Declare training data
# Input data (x) should be a multi-dimensional array.  In this case
# two input features (2 columns) with multiple rows of data.
x = np.array([[3, 7], [12, 20], [23, 24], [38, 32], [44, 51],
             [54, 54], [66, 78], [74, 87], [86, 78], [94, 102]])
# Output data (y) / dependent variables.  The number of rows
# in the output data should match the number of rows in the input data.
y = np.array([3, 22, 18, 31, 55, 41, 37, 67, 66, 82])

# Create a new LinearRegression object.
model = LinearRegression()
# Train the model.
model.fit(x, y)
# Output the model intercept and slope.
print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)
# Use the model to generate predictions.
y_pred = model.predict(x)
# Output the predictions.
print("{0:6}\t{1:6}\t{2:6}\t{3:6}".format("x_0", "x_1", "y","y_pred"))
for i in range(0, 10):
    print("{0:6}\t{1:6}\t{2:6}\t{3:6.0f}".format(x[i, 0], x[i, 1], y[i], y_pred[i]))


# Plotting
plt.scatter(x[:,0], y, color='blue', label='Actual')
plt.scatter(x[:,0], y_pred, color='red', label='Predicted')

# Plotting the regression line
plt.plot(x[:,0], y_pred, color='green', linewidth=2, label='Regression Line')

plt.xlabel('Feature 1')
plt.ylabel('Output')
plt.title('Linear Regression')
plt.legend()
plt.grid(True)
plt.show()