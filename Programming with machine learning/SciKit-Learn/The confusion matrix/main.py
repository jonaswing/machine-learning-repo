# import the sklearn datasets and confusion_matrix
from sklearn import datasets
from sklearn.metrics import confusion_matrix
# import numpy and pandas
import pandas as pd
import numpy as np

# Loads the iris dataset
data, target = datasets.load_iris(return_X_y=True)
# Generates random classifications to simulate a classifier.
# The same number of values are generated as in target.
# The values in target are in the range 0 to 2.  The random
# values are generated in the same range.
results = np.random.randint(3,size=(len(target)))
# Generate a confusion matrix
cm = confusion_matrix(target, results)
# Display the confusion matrix
print("Confusion matrix:\n", cm)


# import the SKLearn classification_report
from sklearn.metrics import classification_report

# Generate a classification report
cr = classification_report(target, results)
# Display the confusion matrix
print("Classification report:\n\n", cr)