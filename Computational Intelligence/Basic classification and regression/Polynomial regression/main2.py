import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# Declare training data
x = np.linspace(1, 100, 10).reshape((-1, 1))
y = np.array([20, 34, 46, 10, 15, 17, 46, 66, 77, 82])

# Create a new PolynomialFeatures object.
transformer = PolynomialFeatures(degree=2, include_bias=False)
# Use it to transform the x values.
x_trans = transformer.fit_transform(x)

# Create a new LinearRegression object.
model = LinearRegression()
# Train the model.
model.fit(x_trans, y)

# Use the model to generate predictions.
y_pred = model.predict(x_trans)

# Plot the original data points
plt.scatter(x, y, color='blue', label='Original data')
# Plot the regression curve
plt.plot(x, y_pred, color='red', label='Polynomial regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Regression')
plt.legend()
plt.grid(True)
plt.show()
