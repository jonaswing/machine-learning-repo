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
# Split the data into training and test data with 20% of the data allocated
# to the test set. Using a specific random_state ensure reproducible results.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)


# Create and train a new classification tree (DecisionTreeClassifier)
# model using the training data.
model = DecisionTreeClassifier(random_state=1)
model.fit(X_train, y_train)


print("Input feature names:\n", model.feature_names_in_)
print("Number of input features:\n", model.n_features_in_)
print("Classes: ", model.classes_)
print("Number of classes:\n", model.n_classes_)
print("Outputs:\n", model.n_outputs_)

print("Feature importances:\n", model.feature_importances_)


# Use the model to predict the output values for the training data.
y_pred_train = model.predict(X_train)

# Output metrics to determine the model's performance.
print("Training accuracy:  ", accuracy_score(y_train,y_pred_train))
print("Training confusion matrix:\n",confusion_matrix(y_train,y_pred_train))
print("Training classification report:\n", classification_report(y_train,y_pred_train))


# Use the model to predict the output values for the test data.
y_pred_test = model.predict(X_test)

# Output metrics to determine the model's performance.
print("\nTest accuracy:  ", accuracy_score(y_test,y_pred_test))
print("Test confusion matrix:\n",confusion_matrix(y_test,y_pred_test))
print("Test classification report:\n", classification_report(y_test,y_pred_test))

