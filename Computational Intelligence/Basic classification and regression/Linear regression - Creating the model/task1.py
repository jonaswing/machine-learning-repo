import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


x = np.array([23, 27, 32, 10, 4, 37, 28, 8, 15, 12, 21, 29, 21, 19, 17, 26]).reshape((-1, 1))
y = np.array([46, 81, 64, 20, 7, 76, 55, 15, 29, 40, 64, 86, 45, 37, 35, 78])


model = LinearRegression()
model.fit(x, y)


# R squared of model
r_sq = model.score(x, y)
print("R squared: ", r_sq)

# Calculate and output the sum of squared errors.
SSE = sum((y - model.predict(x)) ** 2)
print("SSE:  ", SSE)


# ///
# Plot the data points
plt.scatter(x, y, color='blue', label='Data Points')

# Plot the linear regression line
plt.plot(x, model.predict(x), color='red', label='Linear Regression Line')

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()

# Show plot
plt.show()

