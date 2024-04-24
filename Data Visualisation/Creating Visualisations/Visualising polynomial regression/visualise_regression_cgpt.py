import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Load models
with open('linear_regression_demo.mdl', 'rb') as f:
    linear_model = pickle.load(f)

with open('polynomial_regression_demo.mdl', 'rb') as f:
    polynomial_model = pickle.load(f)

# Load test data
linear_test_x = pd.read_csv('linear_test_x.csv', header=None)
polynomial_test_x = pd.read_csv('polynomial_test_x.csv', header=None)
test_y = pd.read_csv('linear_and_polynomial_test_y.csv', header=None)

# Perform predictions
linear_predictions = linear_model.predict(linear_test_x)
polynomial_predictions = polynomial_model.predict(polynomial_test_x)

# Create figure
plt.figure(figsize=(19.20, 10.80), dpi=100)
plt.rc('font', size=24)

# Scatter plot
plt.scatter(linear_test_x.iloc[:, 0], test_y, label='Data Points')

# Sort the values for better visualization of regression lines
sorted_linear_test_x = np.sort(linear_test_x.iloc[:, 0])
sorted_polynomial_test_x = np.sort(polynomial_test_x.iloc[:, 0])

# Linear regression line
plt.plot(sorted_linear_test_x, linear_predictions, color='red', label='Linear Regression')

# Polynomial regression line
plt.plot(sorted_polynomial_test_x, polynomial_predictions, color='green', label='Polynomial Regression')

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Show plot
plt.show()
