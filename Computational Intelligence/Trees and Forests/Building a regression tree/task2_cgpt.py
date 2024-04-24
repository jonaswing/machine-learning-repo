# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score


# Load the dataset
song_data = pd.read_csv("song_data.csv")

# Data preprocessing
# Assuming you have handled any missing values and categorical variables appropriately

# Split data into features (X) and target (y)
X = song_data.drop(columns=['song_popularity', 'song_name'])
y = song_data['song_popularity']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Define hyperparameters to tune
param_grid = {
    'max_depth': [None, 5, 10, 15],  # Try different values for maximum depth
    'min_samples_split': [2, 5, 10],  # Try different values for minimum samples required to split a node
    'min_samples_leaf': [1, 2, 4]  # Try different values for minimum samples required to be at a leaf node
}


# Train the regression tree model
reg_tree = DecisionTreeRegressor(random_state=42)
# Grid search cross-validation
grid_search = GridSearchCV(estimator=reg_tree, param_grid=param_grid, cv=5, scoring='neg_root_mean_squared_error')
grid_search.fit(X_train, y_train)

# Best hyperparameters
best_params = grid_search.best_params_
print("Best Hyperparameters:", best_params)

# Train the model with best hyperparameters
best_reg_tree = grid_search.best_estimator_
best_reg_tree.fit(X_train, y_train)

# Evaluate the model
y_pred = best_reg_tree.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error (RMSE) with best hyperparameters:", rmse)

# Calculate R-squared
r2 = r2_score(y_test, y_pred)
print("R-squared (Coefficient of Determination):", r2)
