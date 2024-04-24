import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier


# Read the data from a file
dataset = pd.read_csv("heart.csv")
# Assign all columns, except the "target" column to x
X = dataset.drop("target", axis=1).drop("fbs", axis=1).drop("thal", axis=1).drop("ca", axis=1)
# Assign only the "target" column to y
y = dataset["target"]


# Split the data into training and test data with 10% of the data allocated
# to the test set.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1)

model = DecisionTreeClassifier(random_state=1,
                               min_samples_split=3)
model.fit(X_train,y_train)

# Use the model to predict the output values for the training data.
y_pred_train = model.predict(X_train)
# Use the model to predict the output values for the test data.
y_pred_test = model.predict(X_test)


# Output metrics to determine the model's performance.
print("Training accuracy:  ", accuracy_score(y_train,y_pred_train))
print("Test accuracy:  ", accuracy_score(y_test,y_pred_test))


# Provide names for the input features.
feature_names = X.columns.values.tolist()
# Output the tree structure as text. The classification
# weights (supporting numbers for each class) will be displayed along with the class.  If the weights are not required, the show_weights argument may be excluded or set to False.
structure = tree.export_text(model, feature_names=feature_names, show_weights=True)
print("Tree structure:\n\n", structure)