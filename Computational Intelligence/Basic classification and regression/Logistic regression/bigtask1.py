import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the dataset
data = np.genfromtxt('possum.csv', delimiter=',', dtype=None, encoding=None, names=True)

# Extract features and labels
X = data[['hdlngth']]  # Feature is hdlngth
y = data['totlngth']  # Target variable to do predictions on


# Split the entire dataset into train, test, and validation sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
# Split the test set into validation set and test set
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Reshape X_train
X_train = X_train.reshape(-1, 1)

# Check data types
print(data.dtypes)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

print(np.min(y))
print(np.max(y))

# Visualize data
plt.scatter(X_train, y_train, color='blue', label='Train data')



# Test model


