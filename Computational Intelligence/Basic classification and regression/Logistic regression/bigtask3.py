import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures


data = np.genfromtxt('possum.csv', delimiter=',', names=True)


x = np.column_stack((data['hdlngth'], data['taill']))
y = data['totlngth']

# Split data into train and test
x_train, x_test_val, y_train, y_test_val = train_test_split(x, y, test_size=0.2, random_state=42)

# Split test into test and validation
x_val, x_test, y_val, y_test = train_test_split(x_test_val, y_test_val, test_size=0.5, random_state=42)


# Train model
model = LinearRegression()
model.fit(x_train, y_train)

# Predict on validation set
y_val_pred = model.predict(x_val)

# Evaluate model
val_score = model.score(x_val, y_val)
print("Validation R-squared score:", val_score)

# Plot actual vs predicted for validation set
plt.scatter(y_val, y_val_pred)
plt.plot(y_val, y_val, color='red')  # plot the diagonal line
plt.xlabel('Actual Total Length')
plt.ylabel('Predicted Total Length')
plt.title('Actual vs Predicted Total Length (Validation Set)')
plt.show()