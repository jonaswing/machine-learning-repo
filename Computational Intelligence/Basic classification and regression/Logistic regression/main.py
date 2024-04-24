# Import numpy and LogisticRegression from sklearn.linear_model
import numpy as np
from sklearn.linear_model import LogisticRegression
# Import classification_report and confusion_matrix from sklearn.metrics
from sklearn.metrics import classification_report, confusion_matrix

# Declare training data
# Input data (x) should be a multi-dimensional array.  In this case
# a single input feature (1 column) with multiple rows of data.
# The data consists of the values 1 to 10.
x = np.arange(10).reshape(-1, 1)
# Output data (y) / dependent variables.  The number of rows
# in the output data should match the number of rows in the input data.
# In this case 0 represents the negative class and 1 the positive class.
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])


# Create a new LogisticRegression object.
model = LogisticRegression(solver='liblinear', random_state=0, C=10.0)
# Train the model.
model.fit(x, y)
# Output the model intercept, slope, the classes in the model
# and the model's predicted probabilities.
print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)
# Output the model classes and predicted probabilities.
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