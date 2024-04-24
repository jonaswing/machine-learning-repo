import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier


# Read the data from a file
dataset = pd.read_csv("heart.csv")
# Assign all columns, except the "target" column to x
X = dataset.drop("target", axis=1)
# Assign only the "target" column to y
y = dataset["target"]
# Split the data into training and test data with 10% of the data allocated
# to the test set.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1)


# Train a model with a ccp_alpha of 0.01206633
model = DecisionTreeClassifier(random_state=1, ccp_alpha=0.01206633)
model.fit(X_train,y_train)
# Use the model to predict the output values for the training data.
y_pred_train = model.predict(X_train)
# Use the model to predict the output values for the test data.
y_pred_test = model.predict(X_test)

# Output metrics to determine the model's performance.
print("Training accuracy:  ", accuracy_score(y_train,y_pred_train))
print("Test accuracy:  ", accuracy_score(y_test,y_pred_test))
