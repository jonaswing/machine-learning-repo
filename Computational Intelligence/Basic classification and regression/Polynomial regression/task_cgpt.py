import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# Data
data = {
    'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Injuries': [20, 18, 12, 7, 6, 6, 12, 15, 16, 18, 24, 25]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plotting the data
plt.figure(figsize=(8, 5))
plt.scatter(df['Month'], df['Injuries'], color='blue', label='Data')
plt.xlabel('Month')
plt.ylabel('Number of Injuries')
plt.title('Skiing Injuries Over Months')
plt.grid(True)
plt.legend()

# Linear Regression
X_linear = df[['Month']]
y_linear = df['Injuries']
linear_reg = LinearRegression()
linear_reg.fit(X_linear, y_linear)
y_linear_pred = linear_reg.predict(X_linear)
plt.plot(X_linear, y_linear_pred, color='red', label='Linear Regression')

# Polynomial Regression
X_poly = df[['Month']]
y_poly = df['Injuries']
poly_features = PolynomialFeatures(degree=3)  # Using degree 3 for polynomial regression
X_poly_transformed = poly_features.fit_transform(X_poly)
poly_reg = LinearRegression()
poly_reg.fit(X_poly_transformed, y_poly)
y_poly_pred = poly_reg.predict(X_poly_transformed)
plt.plot(X_poly, y_poly_pred, color='green', label='Polynomial Regression (deg=3)')

plt.legend()
plt.show()

# Calculating SSE
SSE_linear = mean_squared_error(y_linear, y_linear_pred) * len(y_linear)
SSE_poly = mean_squared_error(y_poly, y_poly_pred) * len(y_poly)

print("SSE of Linear Regression:", SSE_linear)
print("SSE of Polynomial Regression (deg=3):", SSE_poly)
