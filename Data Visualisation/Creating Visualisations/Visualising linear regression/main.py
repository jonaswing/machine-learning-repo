# Import numpy and LinearRegression from sklearn.linear_model
import numpy as np
from sklearn.linear_model import LinearRegression
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Declare training data
# Input data (x) should be a multi-dimensional array. In this case
# a single input feature (1 column) with multiple rows of data.
x = np.array([3, 12, 23, 38, 44, 54, 66, 74, 86, 94]).reshape((-1, 1))
# Output data (y) / dependent variables. The number of rows
# in the output data should match the number of rows in the input data.
y = np.array([3, 22, 18, 31, 55, 41, 37, 67, 66, 82])

# Create a new LinearRegression object.
model = LinearRegression()
# Train the model.
model.fit(x, y)
# Use the model to generate predictions.
y_pred = model.predict(x)


# Generate a scatter plot of the x and y values.
plt.scatter(x, y, color="blue")
# Draw the linear regression line.
plt.plot(x, y_pred, color="red",linewidth=2)
# Display the Figure.
plt.show()


