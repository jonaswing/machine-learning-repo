import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


# Import dataset
data = pd.read_csv('updated_water_potability.csv')
data = pd.DataFrame(data)


# PRE PROCESSING
# Round columns to three decimals
data = data.round(3)
# Round the 'ph' column to one decimal
data['ph'] = data['ph'].round(1)


# CLASSIFICATION MODEL

# TARGET
# Choosing target to predict for classification
X_c = data.drop('Potability', axis=1)
y_c = data['Potability']

# SPLITTING
# Split into training and test
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_c, y_c, test_size=0.2, random_state=1)

# TRAINING
# Train model
model_c = RandomForestClassifier()
model_c.fit(X_train_c, y_train_c)

# PREDICTIONS
predictions_classification = model_c.predict(X_test_c)

# EVALUATION
accuracy_classification = accuracy_score(y_test_c, predictions_classification)
print("Accuracy classification potability:", accuracy_classification)


# REGRESSION MODEL

# TARGET
# Choosing target to predict for regression
X_r = data.drop('ph', axis=1)
y_r = data['ph']


# SPLITTING
# Split into training and test
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_r, y_r, test_size=0.2, random_state=1)

# TRAINING
# Train model
model_r = RandomForestRegressor()
model_r.fit(X_train_r, y_train_r)

# PREDICTIONS
predictions_regression = model_r.predict(X_test_r)

# EVALUATION
r_squared = r2_score(y_test_r, predictions_regression)
print("R-squared regression ph:", r_squared)

