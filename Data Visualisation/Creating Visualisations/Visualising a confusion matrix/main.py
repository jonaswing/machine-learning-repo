# Import numpy and LogisticRegression from sklearn.linear_model
import numpy as np
from sklearn.linear_model import LogisticRegression
# Import classification_report and confusion_matrix from sklearn.metrics
from sklearn.metrics import classification_report, confusion_matrix
# Import matplotlib.pyplot
import matplotlib.pyplot as plt


# Declare training data
# Input data (x) should be a multi-dimensional array. In this case
# a single input feature (1 column) with multiple rows of data.
# The data consists of the values 1 to 10.
x = np.arange(10).reshape(-1, 1)
# Output data (y) / dependent variables. The number of rows
# in the output data should match the number of rows in the input data.
# In this case 0 represents the negative class and 1 the positive class.
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Create a new LogisticRegression object.
model = LogisticRegression(solver='liblinear', random_state=0, C=10.0)
# Train the model.
model.fit(x, y)
# Use the model to generate predictions.
y_pred = model.predict(x)
# Generate the confusion matrix for the model
cm = confusion_matrix(y, model.predict(x))


fig, ax = plt.subplots()
# Display the confusion matrix data as a two-dimensional image
# using the seismic colormap.
im = ax.imshow(cm, cmap="seismic")
# Set the axes ticks range and labels.
ax.xaxis.set(ticks=(0, 1), ticklabels=("Predicted 0s", "Predicted 1s"))
ax.yaxis.set(ticks=(0, 1), ticklabels=("Actual 0s", "Actual 1s"))
# Set the limits of the y axis to 1.5 and -0.5.
ax.set_ylim(1.5, -0.5)
# Iterate over the values in the confusion matrix.
for i in range(2):
    for j in range(2):
        # Display each value in the confusion matrix in the center of it's grid
        # block.
        ax.text(j, i, cm[i, j], ha="center", va="center", color="white")
# Add a colorbar.
fig.colorbar(im)
# Display the Figure.
plt.show()