import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Perform random instance selection
subset_size = 50  # Number of instances to select randomly
random_indices = np.random.choice(X.shape[0], subset_size, replace=False)

# Create the subset
X_subset = X[random_indices]
y_subset = y[random_indices]

# Print the selected instances
print("Selected Instances:")
print(X_subset)

# Optionally, split the subset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_subset, y_subset, test_size=0.2, random_state=42)

# Print the shapes of the training and testing sets
print("\nShapes of Training and Testing Sets:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)
