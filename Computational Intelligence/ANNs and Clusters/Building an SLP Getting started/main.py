import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Load the iris data set.
data_set = load_iris()
# Setting the data argument of the iris set to be the independent variables
# and the target attribute to be the dependent variable.
X = data_set.data
y = data_set.target
# Generate training and test data sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1)


# Create a Perceptron (SLP) model.  Verbose is set to 3 to allow update message to
# be displayed during training.  Setting n_jobs to 2 allows the model to use 2
# CPUs during the training process.  random_state is set to 1 to ensure reproducibility.
model = Perceptron(verbose=3, n_jobs=2, random_state=1)
model.fit(X_train, y_train)
# Generate predictions for the test data.
y_pred_test = model.predict(X_test)
# Output the accuracy of the model on the test_data to 3 decimal digits.
print("Accuracy:  {0:.3f}".format(accuracy_score(y_test, y_pred_test)))


# Generate a dataframe which contains the class labels instead of just
# numeric predictions.  This allows for a simple visual comparison of the results.
# Since the predictions are all numeric values from the data set's target_names
# attribute, we can use the predictions to retrieve the associated labels.
comparison = pd.DataFrame({ "original y": y_test,
                            "predicted y": y_pred_test,
                            "class": data_set.target_names[y_test],
                            "prediction": data_set.target_names[y_pred_test]},
                          columns=["original y", "predicted y", "class", "prediction"])





