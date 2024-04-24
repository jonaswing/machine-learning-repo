from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
import pydotplus
import graphviz

# Load the IRIS data set.
iris = load_iris()

# Split the data into training and test data with 10% of the data allocated
# to the test set.
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.10, random_state=1)

# Train a default DecisionTreeClassifier.
# random_state is set to 1 to ensure reproducibility.
model = DecisionTreeClassifier(random_state=1)
model.fit(X_train, y_train)


# Define the feature names to be used when creating the DOT representation.
feature_names = ["sepal length", "sepal width", "petal length", "petal width"]
# Use the export_graphviz() function to generate the DOT representation.
dot_data = tree.export_graphviz(model,
                                feature_names=feature_names,
                                class_names=iris.target_names,
                                filled=True,
                                rounded=True)
# Output the DOT representation.
# This isn't necessary, but is done here to demonstrate
# what it looks like.
print("DOT representation:\n", dot_data)


# Call graph_from_dot_data to convert the DOT representation
# to a Dot class/container.
graph = pydotplus.graph_from_dot_data(dot_data)
# Set the dots per inch to 300
graph.dpi = 300
# Output a .png file of the visualisation to the
# path specified. In this case, in the same directory
# as the script file.
graph.write_png("ClassificationTree.png")


