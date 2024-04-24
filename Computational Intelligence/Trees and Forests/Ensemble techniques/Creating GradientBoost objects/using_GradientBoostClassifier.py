import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error


dataset = pd.read_csv("water_potability.csv")
dataset.dropna(inplace=True)
X = dataset.drop("Potability", axis=1)
y = dataset["Potability"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20, random_state=1)
model = GradientBoostingClassifier(random_state=1, learning_rate=0.1, max_depth=10, n_estimators=50)
model.fit(X_train,y_train)
y_pred_test = model.predict(X_test)
print("Accuracy:  ", accuracy_score(y_test,y_pred_test))

