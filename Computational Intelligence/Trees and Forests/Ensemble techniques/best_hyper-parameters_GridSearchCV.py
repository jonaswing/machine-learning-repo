import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
# Import the GridSearchCV class from sklearn's model_selection module.
from sklearn.model_selection import GridSearchCV


dataset = pd.read_csv("Building a RandomForestClassifier/water_potability.csv")
print("Shape before drop:", dataset.shape)
# Drop any entries with missing values and overwrite the existing dataset
# with the revised one.
dataset.dropna(inplace=True)
print("Shape after drop:", dataset.shape)

# Did this because finding hyperparameters took forever with the entire dataset
#dataset = dataset.head(50)

X = dataset.drop("Potability", axis=1)
y = dataset["Potability"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)


# Declare a dictionary of hyper-parameters for the GridSearchCV object to test.
parameters = {
     "n_estimators": [5, 10, 50, 100, 250, 500, 750, 1000],
     "max_depth": [2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, None]

}


# Create a default RandomForestClassifier.  random_state is set to 1
# for the sake of presenting consistent results.
model = RandomForestClassifier(random_state=1)
# Create a GridSearchCV object based on the model, using the provided hyperparameters.
# The default cross-validation (cv) value of 5 is used.
cv = GridSearchCV(model, parameters, verbose=0)
# Perform the grid search.
cv.fit(X_train, y_train)
# Output the best performing results.
print("The best performing hyperparameters are: ", cv.best_params_)


non_optimised = RandomForestClassifier(random_state=1)
optimised = RandomForestClassifier(random_state=1, max_depth=2, n_estimators=5)
non_optimised.fit(X_train, y_train)
optimised.fit(X_train, y_train)
y_pred_test_non_optimised = non_optimised.predict(X_test)
y_pred_test_optimised = optimised.predict(X_test)
print("Non-optimised test accuracy:  ", accuracy_score(y_test, y_pred_test_non_optimised))
print("Optimised test accuracy:  ", accuracy_score(y_test, y_pred_test_optimised))


