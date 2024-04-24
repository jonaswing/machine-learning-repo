from sklearn.datasets import fetch_california_housing
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_validate

# Retrieve the California housing data set
X, y = fetch_california_housing(as_frame=False, return_X_y=True)


# Create the basic MLPRegressor object to use in the cross validation.
model = MLPRegressor(random_state=1,
                      max_iter=5000,
                      hidden_layer_sizes=(6,))

# Perform 10-fold cross-validation, using mean_squared_error.  The process
# will output its progress (verbose=3) and return the various versions
# of the estimator (models) created during the cross-validation process.
cv_results = cross_validate(model, X, y,
                            cv=10, verbose=3,
                            scoring="neg_mean_squared_error",
                            return_estimator=True)

# Output the results.
for current in cv_results.keys():
    print("{0}:".format(current))
    print(cv_results[current])
    print()


# Specificy the index of the model (in this case the first one)
# to retrieve from the list of estimators.
model = cv_results["estimators"][0]

