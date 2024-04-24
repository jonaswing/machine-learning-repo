# Other imports
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd


# Import dataset
data = pd.read_csv('updated_water_potability.csv')
data = pd.DataFrame(data)


# PRE PROCESSING
# Round columns to three decimals
data = data.round(3)
# Round the 'ph' column to one decimal
data['ph'] = data['ph'].round(1)

# TARGET
# Choosing target to predict for regression
X_r = data.drop('ph', axis=1)
y_r = data['ph']

# Splitting
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_r, y_r, test_size=0.2, random_state=1)

# Create a pipeline with preprocessing and model
model_r = make_pipeline(StandardScaler(), RandomForestRegressor())

# Train the model
model_r.fit(X_train_r, y_train_r)

# Make predictions
predictions_regression = model_r.predict(X_test_r)

# Evaluate the model
r_squared = r2_score(y_test_r, predictions_regression)
print("R-squared regression ph:", r_squared)
