from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the iris data set.
data_set = load_iris()
# Setting the data argument of the iris set to be the independent variables
# and the target attribute to be the dependent variable.
X = data_set.data
y = data_set.target

# Generate training and test data sets.
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.10, random_state=1)


# Create a MLPClassifier which will iterate over a maximum of 5000 epochs.
# It uses a preset random seed, for reproducibility and generates output
# as it trains/fits the model.  The model has a single hidden layer with 10 nodes.
model = MLPClassifier(random_state=1,
                      max_iter=5000,
                      verbose=True,
                      hidden_layer_sizes=(10,))

model.fit(X_train, y_train)
# Generate predictions for the test data.
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
# Output the accuracy of the model on the test_data to 3 decimal digits.
print("Training accuracy:  {0:.3f}".format(accuracy_score(y_train, y_pred_train)))
print("Test accuracy:  {0:.3f}".format(accuracy_score(y_test, y_pred_test)))


# Output the model attributes
print("Model weights per layer:")
for i in range(0, len(model.coefs_)):
    print(" - Layer {0} sets of weights: {1}".format(i, len(model.coefs_[i])))
    print(" - Layer {0} number of weights in set: {1}".format(i, len(model.coefs_[i][0])))
print("\nModel biases per layer:")
for i in range(0, len(model.intercepts_)):
    print(" - Layer {0} number of biases: {1}".format(i, len(model.intercepts_[i])))
#print("Model weights:\n", model.coefs_, "\n")
#print("Model biases:\n", model.intercepts_, "\n")
print("\nNumber of layers: ", model.n_layers_)
print("Number of outputs: ", model.n_outputs_)
print("Output activation function: ", model.out_activation_)
print("Best loss: ", model.best_loss_)
print("Classes: ", model.classes_)
print("Classes: ", model.classes_)

