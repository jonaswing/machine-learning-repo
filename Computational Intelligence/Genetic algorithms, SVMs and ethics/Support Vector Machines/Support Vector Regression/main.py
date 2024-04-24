# Import numpy.
import numpy as np
# Import sklearn dataset library.
from sklearn.datasets import fetch_california_housing
# Import the train_test_split function.
from sklearn.model_selection import train_test_split
# Import the SVR svm model (class).
from sklearn.svm import SVR
# Import the sklearn metrics module to calculate
# the models's mean_squared_error.
from sklearn.metrics import mean_squared_error

# Retrieve the California housing data set
X, y = fetch_california_housing(as_frame=False, return_X_y=True)

# Generate training and test data sets.
X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.10, random_state=1)


# Create SVM classifiers, based on SVR.  Four
# different kernel types are tested with other
# hyperparameters set to their default values.
kernels = ["linear", "poly", "rbf", "sigmoid"]
for kernel in kernels:
    model = SVR(kernel=kernel)
    # Train the model using the training sets.
    model.fit(X_train, y_train)
    # Predict the response for test dataset.
    y_pred = model.predict(X_test)
    # Output the root of the mean_squared_error of the model on
    # the test_data to 3 decimal digits.
    print("{0} kernel test error:  {1:.3f}".format(kernel, np.sqrt(mean_squared_error(y_test,y_pred))))


