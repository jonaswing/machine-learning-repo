import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt


data = {
    'percentage': np.array([33,57,32,90,67,23,55,76,73,38,47,89]).reshape(-1, 1),  # y
    'student_result': np.array([0,1,0,1,1,0,1,1,1,0,1,1])  # x
}


# Create a LogisticRegression object
model = LogisticRegression(solver='liblinear', random_state=0, C=10.0)
# Train model
model.fit(data['percentage'], data['student_result'])
# Make predictions
value_to_predict = np.array([34, 94, 39, 45, 68, ]).reshape(-1,1)
prediction = model.predict(value_to_predict)


print("Score: ", model.score(data['percentage'], data['student_result']))


# Plot the data points
plt.scatter(data['percentage'], data['student_result'], color='black', label='Data Points')
# Plot the logistic regression curve
x_values = np.linspace(0, 100, 100).reshape(-1, 1)
y_values = model.predict_proba(x_values)[:, 1]
plt.plot(x_values, y_values, color='blue', label='Logistic Regression Curve')
plt.scatter(value_to_predict, prediction, color='red', label='Number')


plt.show()