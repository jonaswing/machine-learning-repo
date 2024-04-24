import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Import dataset
data = pd.read_csv('song_data.csv')
df = pd.DataFrame(data)

# Pre-processing
# Remove duplicates
df = df.drop_duplicates(subset=['song_name'])


# Choose target (predict y)
X = df.drop(['song_name', 'song_popularity'], axis=1)
y = df['song_popularity']

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Choose model
model = DecisionTreeRegressor(random_state=1, ccp_alpha=3)

# Train model
model.fit(X_train, y_train)

# Use the model to predict the output values for the test data.
y_pred_train = model.predict(X_train)

# Use the model to predict the output values for the test data.
y_pred_test = model.predict(X_test)


print("\nTraining data scores:")
print("Mean Absolute Error (MAE): ", mean_absolute_error(y_train, y_pred_train))
print("Mean Squared Error (MSE): ", mean_squared_error(y_train, y_pred_train))
print("Root Mean Squared Error (RMSE): ", np.sqrt(mean_squared_error(y_train, y_pred_train)))
print("R-squared (R2): ", r2_score(y_train, y_pred_train))

print("\nTesting data scores:")
print("Mean Absolute Error (MAE): ", mean_absolute_error(y_test, y_pred_test))
print("Mean Squared Error (MSE): ", mean_squared_error(y_test, y_pred_test))
print("Root Mean Squared Error (RMSE): ", np.sqrt(mean_squared_error(y_test, y_pred_test)))
print("R-squared (R2): ", r2_score(y_test, y_pred_test))


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
