import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt


x = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(-1,1)
y = np.array([20,18,12,7,6,6,12,15,16,18,24,25])

# Linear model
linear_model = LinearRegression()

linear_model.fit(x, y)

linear_pred = linear_model.predict(x)

print("\nLinear regression model")
# Model score (r squared)
r_sq = linear_model.score(x, y)
print("Score", r_sq)
# Linear SSE (Sum of Squared Errors)
SSE = sum((y - linear_pred) ** 2)
print("Linear SSE:  ", SSE)




# Polynomial
# Create a new PolynomialFeatures object.
transformer = PolynomialFeatures(degree=5, include_bias=False)
# Use it to transform the x values.
x_trans = transformer.fit_transform(x)

# Create a new LinearRegression object.
polynomial_model = LinearRegression()
# Train the model.
polynomial_model.fit(x_trans, y)

# Use the model to generate predictions.
polynomial_pred = polynomial_model.predict(x_trans)


print("\nPolynomial regression model")
# Model score (r squared)
pr_sq = polynomial_model.score(x_trans, y)
print("Score: ", pr_sq)
# Linear SSE (Sum of Squared Errors)
SSE = sum((y - polynomial_pred) ** 2)
print("Linear SSE:  ", SSE)


print("\nConclusion: The polynomial regression model is more accurate in this scenario, "
      "\nbecause it has higher score (r squared or coefficient), and lower SSE)")


# Show plot
plt.scatter(x, y, color='blue', label='data')
plt.plot(x, polynomial_pred, color='red', label='polynomial')
plt.plot(x, linear_pred, color='green', label='linear')
plt.title('Comparing linear and polynomial')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()






