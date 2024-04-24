from sklearn import datasets
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics


data = datasets.load_iris()


# train test split
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=1)


model = SVC(kernel="linear")
# Train the model using the training sets.
model.fit(X_train, y_train)
# Predict the response for test dataset.
y_pred = model.predict(X_test)

# Generate and output the accuracy, precision and recall metrics.
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))



