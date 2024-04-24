import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

data = {
    'percentage': np.array([33,57,32,90,67,23,55,76,73,38,47,89]),  # y
    'student_result': np.array([0,1,0,1,1,0,1,1,1,0,1,1]).reshape(-1, 1)  # x
}

# Create a LogisticRegression object
model = LogisticRegression(solver='liblinear', random_state=0)
# Train model
model.fit(data['student_result'], data['percentage'])

# Make predictions on the training data
y_pred = model.predict(data['student_result'])

# Plot the data points
plt.scatter(data['student_result'], data['percentage'], color='black', label='Data')

# Plot the logistic regression curve
x_values = np.linspace(0, 1, 100).reshape(-1, 1)
y_values = model.predict(x_values)
plt.plot(x_values, y_values, color='blue', label='Logistic Regression Curve')

plt.xlabel('Student Result')
plt.ylabel('Percentage')
plt.title('Logistic Regression')
plt.legend()
plt.grid(True)
plt.show()

print("Score: ", model.score(data['student_result'], data['percentage']))
