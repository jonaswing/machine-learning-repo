from sklearn import datasets
# Import sklearn dataset library.
from sklearn import datasets
# Import the train_test_split function.
from sklearn.model_selection import train_test_split
# Import the SVC svm model (class).
from sklearn.svm import SVC
# Import the sklearn metrics module to calculate
# the model's accuracy, precision and recall.
from sklearn import metrics


# Load the dataset.
data = datasets.load_breast_cancer()


# Split the dataset into a training set (80%) and test set (20%),
# with a random_state of 1 to ensure reproducibility.
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=1)

# Create an SVM classifier, based on SVC.  The SVC is created
# using the default settings with a linear kernel.
model = SVC(kernel="linear")
# Train the model using the training sets.
model.fit(X_train, y_train)
# Predict the response for test dataset.
y_pred = model.predict(X_test)

# Generate and output the accuracy, precision and recall metrics.
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))

