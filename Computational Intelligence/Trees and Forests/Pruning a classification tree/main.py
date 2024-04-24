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
# Train the initial, unpruned model
model = DecisionTreeClassifier(random_state=1)
model.fit(X_train,y_train)
# Use the model to predict the output values for the test data.
y_pred_test = model.predict(X_test)


# Initial variables used during iteration to store the best accuracy
# and ccp_alpha values, as well as the current ccp_alpha value.
best_accuracy = accuracy_score(y_test,y_pred_test)
current_accuracy = best_accuracy
best_alpha = 0
ccp_alpha = 0

# Loop to iterate through various ccp_alpha values
while ccp_alpha < 1:
    # Each iteration uses a ccp_alpha value that is 0.00000001 greater than the previous iteration.
    # Other iterator values which are either smaller or larger may be used.  This will have an effect
    # on both the time it takes to find the optimal alpha value, as well as on the granularity of the
    # value found.
    ccp_alpha += 0.001

    # Train a model with this ccp_alpha value.
    model = DecisionTreeClassifier(random_state=1,
                               ccp_alpha=ccp_alpha)
    model.fit(X_train,y_train)
    # Test the current model's accuracy on the test data set.
    y_pred_test = model.predict(X_test)
    current_accuracy = accuracy_score(y_test,y_pred_test)
    # If the current value is more accurate than the previous best performing model,
    # replace the highest accuracy with the new highest accuracy and updates the best_alpha value
    # with the current one.
    if current_accuracy > best_accuracy:
        best_accuracy = current_accuracy
        best_alpha = ccp_alpha
        print("Accuracy: ", best_accuracy)
        print("ccp_alpha: {:.8f}".format(best_alpha))