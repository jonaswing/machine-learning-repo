# Step 1: Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, accuracy_score

# Step 2: Load the dataset
data = pd.read_csv("possum.csv")  # Make sure to provide the correct path

# Step 3: Preprocess the data
# There are missing values represented by "NA" in the dataset. Let's drop those rows.
data = data.dropna()

# Step 4: Split the data into training and testing sets
X = data[['hdlngth']]  # Features
y = data['totlngth']   # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train models
# Linear Regression
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)

# Polynomial Regression (degree=2)
poly_features = PolynomialFeatures(degree=2)
X_train_poly = poly_features.fit_transform(X_train)
X_test_poly = poly_features.transform(X_test)

poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)

# Step 6: Evaluate models
# Predictions
linear_pred = linear_reg.predict(X_test)
poly_pred = poly_reg.predict(X_test_poly)

# Mean Squared Error
linear_mse = mean_squared_error(y_test, linear_pred)
poly_mse = mean_squared_error(y_test, poly_pred)

print("Linear Regression Mean Squared Error:", linear_mse)
print("Polynomial Regression Mean Squared Error:", poly_mse)

# Step 7: Choose the best performing model
# In this case, we'll choose the model with the lower Mean Squared Error
if linear_mse < poly_mse:
    print("Linear Regression performs better.")
else:
    print("Polynomial Regression performs better.")