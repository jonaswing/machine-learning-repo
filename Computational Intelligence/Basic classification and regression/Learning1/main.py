from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Assume X contains your features and y contains your target variable
x = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y = np.array([1,2,3,4,5,6,7,8,9,10])
# X_train, X_test, y_train, y_test are already defined for test split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Further split the training data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Create and train the model using the training set
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the validation set
y_val_pred = model.predict(X_val)
val_mse = mean_squared_error(y_val, y_val_pred)
print("Validation MSE:", val_mse)

# Once you're satisfied with the model's performance on the validation set, you can evaluate it on the test set
y_test_pred = model.predict(X_test)
test_mse = mean_squared_error(y_test, y_test_pred)
print("Test MSE:", test_mse)

# Calculate Sum of Squared Errors (SSE)
sse = sum((true - pred) ** 2 for true, pred in zip(y_test, y_test_pred))
print("Sum of Squared Errors (SSE):", sse)
