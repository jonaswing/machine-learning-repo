import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


# Read the data from a file
dataset = pd.read_csv("song_data.csv")
# Assign all columns, except the "Y house price unit of area" column to x
X = dataset.drop(["song_popularity", "song_name", "instrumentalness"], axis=1)
# Assign only the "Y house price of unit area" column to y
y = dataset["song_popularity"]

# Split the data into training and test data with 20% of the data allocated
# to the test set.  Setting the random_state to a specific integer value ensures that the
# data sets are created in a reproducible fashion.
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=1)

# Create and train a new regression tree (DecisionTreeRegressor)
# model using the training data.
model = DecisionTreeRegressor(random_state=1)
model.fit(X_train,y_train)


# Use the model to predict the output values for the training and test data.
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
# Output metrics to determine the model's performance.
print("Mean absolute error for training data:  ", mean_absolute_error(y_train, y_pred_train))
print("Root Mean Squared Error for training data:  ", np.sqrt(mean_squared_error(y_train, y_pred_train)))
print("Mean absolute error for test data:  ", mean_absolute_error(y_test, y_pred_test))
print("Root Mean Squared Error for test data:  ", np.sqrt(mean_squared_error(y_test, y_pred_test)))

print()

# Initial variables used during iteration to store the best root mean squared error
# and ccp_alpha values, as well as the current ccp_alpha value.
best_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
current_rmse = best_rmse
best_alpha = 0

# Retrieve the alpha and impurity values using cost_complexity_pruning_path().
path = model.cost_complexity_pruning_path(X_train,y_train)

# Output the starting accuracy and ccp_alpha values
print("Initial Root Mean Squared Error: ", best_rmse)
print("Default ccp_alpha: {:.8f}".format(best_alpha))

# Loop to iterate through various ccp_alpha values
for ccp_alpha in path.ccp_alphas:
    # Train a model with this ccp_alpha value.
    model = DecisionTreeRegressor(random_state=1,
                               ccp_alpha=ccp_alpha)
    model.fit(X_train,y_train)
    # Test the current model's accuracy on the test data set.
    y_pred_test = model.predict(X_test)
    current_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
    # If the current value is more accurate than the previous best performing model,
    # replace the highest accuracy with the new highest accuracy and updates the best_alpha value
    # with the current one.
    if current_rmse < best_rmse:
        best_rmse = current_rmse
        best_alpha = ccp_alpha

# Output the results
print("Final Root Mean Squared Error: ", best_rmse)
print("Best ccp_alpha: {:.8f}".format(best_alpha))

print()

# Train a model with a ccp_alpha of 3.48761707
model = DecisionTreeRegressor(random_state=1,
                               ccp_alpha=3.48761707)
model.fit(X_train,y_train)
# Use the model to predict the output values for the training and test data.
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
# Output metrics to determine the model's performance.
print("Mean absolute error for training data:  ", mean_absolute_error(y_train, y_pred_train))
print("Root Mean Squared Error for training data:  ", np.sqrt(mean_squared_error(y_train, y_pred_train)))
print("Mean absolute error for test data:  ", mean_absolute_error(y_test, y_pred_test))
print("Root Mean Squared Error for test data:  ", np.sqrt(mean_squared_error(y_test, y_pred_test)))


