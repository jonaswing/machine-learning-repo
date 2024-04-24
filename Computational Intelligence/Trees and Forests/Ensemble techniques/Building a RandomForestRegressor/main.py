import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV

dataset = pd.read_csv("water_potability.csv")
# Drop any entries with missing values and overwrite the existing dataset
# with the revised one.
dataset.dropna(inplace=True)
X = dataset.drop("ph", axis=1)
y = dataset["ph"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Declare a dictionary of hyper-parameters for the GridSearch to test.
parameters = {
     "n_estimators": [5, 10, 50, 100, 250, 500, 750, 1000],
     "max_depth": [2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, None]
}

# Create a default RandomForestRegressor.  random_state is set to 1
# for the sake of presenting consistent results.
model = RandomForestRegressor(random_state=1)
# Create a GridSearchCV object based on the model, using the provided hyperparameters.
# The default cross-validation (cv) value of 5 is used.
cv = GridSearchCV(model,parameters)
# Perform the grid search.
cv.fit(X_train,y_train)
# Output the best performing results.
print("The best performing hyperparameters are: ", cv.best_params_)