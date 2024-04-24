import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Read the dataset
data = np.genfromtxt('possum.csv', delimiter=',', dtype=None, names=True, encoding=None)

# Extract features and target variable
X = np.column_stack((data['age'], data['hdlngth'], data['skullw'], data['taill'], data['footlgth'], data['earconch'], data['eye'], data['chest'], data['belly']))
y = data['totlngth']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Example prediction
example = [[8, 94.1, 60.4, 36, 74.5, 54.5, 15.2, 28, 36]]  # Adjust with real data
predicted_length = model.predict(example)
print('Predicted total length:', predicted_length)
