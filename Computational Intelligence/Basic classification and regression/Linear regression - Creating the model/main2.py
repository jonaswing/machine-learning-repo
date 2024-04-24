# Import numpy and LinearRegression from sklearn.linear_model
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# Declare training data
# Input data (x) should be a multi-dimensional array.  In this case
# a single input feature (1 column) with multiple rows of data.
x = np.array([3, 12, 23, 38, 44, 54, 66, 74, 86, 94]).reshape((-1, 1))
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
print("\nPredicted response:\n", y_pred)


# Calculate and output the r squared value.
r_sq = model.score(x, y)
print("\nR squared: ", r_sq)

# Calculate and output the sum of squared errors.
SSE = sum((y - y_pred) ** 2)
print("SSE:  ", SSE)


# ///
# Plot the data points
plt.scatter(x, y, color='blue', label='Data Points')

# Plot the linear regression line
plt.plot(x, model.predict(x), color='red', label='Linear Regression Line')

# Plot the predictions
plt.scatter(x, y_pred, color='green', label='Predictions')

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()

# Show plot
plt.show()