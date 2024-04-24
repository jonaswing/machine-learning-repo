import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# Data
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(-1,1)
y = np.array([20,18,12,7,6,6,12,15,16,18,24,25])

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(x, y)
y_pred_linear = linear_model.predict(x)

# Polynomial Regression
poly_transformer = PolynomialFeatures(degree=5, include_bias=False)
x_poly = poly_transformer.fit_transform(x)
poly_model = LinearRegression()
poly_model.fit(x_poly, y)
y_pred_poly = poly_model.predict(x_poly)

# Plot
plt.scatter(x, y, color='blue', label='Data')
plt.plot(x, y_pred_linear, color='red', label='Linear Regression')
plt.plot(x, y_pred_poly, color='green', label='Polynomial Regression (degree=5)')
plt.title('Linear vs Polynomial Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
