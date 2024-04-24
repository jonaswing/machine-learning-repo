import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Retrieve the California housing data set
X, y = fetch_california_housing(as_frame=False, return_X_y=True)

# Generate training and test data sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1)

# Create a MLPRegressor which will iterate over a maximum of 5000 epochs.
# It uses a preset random seed, for reproducibility and generates output
# as it trains/fits the model.  The model has a single hidden layer with 6 nodes.
model = MLPRegressor(random_state=1,
                      max_iter=5000,
                      verbose=True,
                      hidden_layer_sizes=(6,))
model.fit(X_train, y_train)
# Generate predictions for the test data.
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
# Output the accuracy of the model on the test_data to 3 decimal digits.
print("Training error:  {0:.3f}".format(np.sqrt(mean_squared_error(y_train, y_pred_train))))
print("Test error:  {0:.3f}".format(np.sqrt(mean_squared_error(y_test, y_pred_test))))





