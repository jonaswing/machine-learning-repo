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
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.10, random_state=1)


# Using no regularisation.  The default penalty is None.
model = Perceptron(random_state=1)
model.fit(X_train, y_train)
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
print("None train accuracy:  {0:.3f}".format(accuracy_score(y_train, y_pred_train)))
print("None test accuracy:  {0:.3f}".format(accuracy_score(y_test, y_pred_test)))
# Using l1 regularisation
model = Perceptron(random_state=1, penalty="l1")
model.fit(X_train, y_train)
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
print("l1 train accuracy:  {0:.3f}".format(accuracy_score(y_train, y_pred_train)))
print("l1 test accuracy:  {0:.3f}".format(accuracy_score(y_test, y_pred_test)))
# Using l2 regularisation
model = Perceptron(random_state=1, penalty="l2")
model.fit(X_train, y_train)
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
print("l2 train accuracy:  {0:.3f}".format(accuracy_score(y_train, y_pred_train)))
print("l2 test accuracy:  {0:.3f}".format(accuracy_score(y_test, y_pred_test)))
# Using elasticnet regularisation
model = Perceptron(random_state=1, penalty="elasticnet")
model.fit(X_train, y_train)
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
print("elasticnet train accuracy:  {0:.3f}".format(accuracy_score(y_train, y_pred_train)))
print("elasticnet test accuracy:  {0:.3f}".format(accuracy_score(y_test, y_pred_test)))

