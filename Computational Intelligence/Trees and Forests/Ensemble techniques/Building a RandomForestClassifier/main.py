import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier


dataset = pd.read_csv("water_potability.csv")
print("Shape before drop:", dataset.shape)
# Drop any entries with missing values and overwrite the existing dataset
# with the revised one.
dataset.dropna(inplace=True)
print("Shape after drop:", dataset.shape)
X = dataset.drop("Potability", axis=1)
y = dataset["Potability"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)


# RandomForestClassifier
model = RandomForestClassifier(random_state=1)
model.fit(X_train,y_train)
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
print("\nTraining accuracy:  ", accuracy_score(y_train,y_pred_train))
print("Test accuracy:  ", accuracy_score(y_test,y_pred_test))


# DecisionTreeClassifier
model_tree = DecisionTreeClassifier(random_state=1)
model_tree.fit(X_train,y_train)
y_pred_train = model_tree.predict(X_train)
y_pred_test = model_tree.predict(X_test)
print("\nTraining accuracy:  ", accuracy_score(y_train, y_pred_train))
print("Test accuracy:  ", accuracy_score(y_test, y_pred_test))




