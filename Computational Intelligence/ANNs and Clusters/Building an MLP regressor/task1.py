import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


X, y = fetch_california_housing(as_frame=False, return_X_y=True)

# Generate training and test data sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1)


model = MLPRegressor(random_state=1, learning_rate_init=0.0001, alpha=0.1, max_iter=2000, activation='logistic', solver='adam')


model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Output the accuracy of the model on the test_data to 3 decimal digits.
print("Training error:  {0:.3f}".format(np.sqrt(mean_squared_error(y_train, y_pred_train))))
print("Test error:  {0:.3f}".format(np.sqrt(mean_squared_error(y_test, y_pred_test))))

