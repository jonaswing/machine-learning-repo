import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
import numpy as np

dataset = pd.read_csv("water_potability.csv")
# Drop any entries with missing values and overwrite the existing dataset
# with the revised one.
dataset.dropna(inplace=True)
X = dataset.drop("ph", axis=1)
y = dataset["ph"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)


non_optimised = RandomForestRegressor(random_state=1)
optimised = RandomForestRegressor(random_state=1, max_depth=9, n_estimators=500)
non_optimised.fit(X_train,y_train)
optimised.fit(X_train,y_train)
y_pred_test_optimised = optimised.predict(X_test)
print("Optimised test RMSE:  ", np.sqrt(mean_squared_error(y_test, y_pred_test_optimised)))