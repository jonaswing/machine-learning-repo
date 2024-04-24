import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Declare training data
x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Create a new LogisticRegression object.
model = LogisticRegression(solver='liblinear', random_state=0, C=10.0)
# Train the model.
model.fit(x, y)

# Output the model intercept, slope, the classes in the model
# and the model's predicted probabilities.
print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)
print("Model classes: ", model.classes_)
print("Predicted probabilities:\n", model.predict_proba(x))

# Use the model to generate predictions.
y_pred = model.predict(x)
# Output the predictions.
print("Predictions: ", y_pred)
# Output the statistics of the model.
print("Accuracy: ", model.score(x, y))
print("Confusion matrix:\n", confusion_matrix(y, y_pred))
print("\nClassification report:\n", classification_report(y, y_pred))

# Plot the data points
plt.scatter(x, y, color='black', label='Data Points')

# Plot the logistic regression curve
x_values = np.linspace(0, 9, 100).reshape(-1, 1)
y_values = model.predict_proba(x_values)[:, 1]
plt.plot(x_values, y_values, color='blue', label='Logistic Regression Curve')

# Add labels and legend
plt.xlabel('Input Data (x)')
plt.ylabel('Predicted Probability')
plt.title('Logistic Regression')
plt.legend()

# Show plot
plt.show()
