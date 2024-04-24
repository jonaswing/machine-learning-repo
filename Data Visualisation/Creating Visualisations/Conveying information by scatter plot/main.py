import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
# Load the IRIS data set.
iris = load_iris()
features = iris.data.T
plt.rcParams.update({"font.size": 22, "figure.figsize": [19.20, 10.80]})
fig, ax = plt.subplots()

# Create a scatter plot by plotting sepal length and width,
# using petal width as the size and the target variable as
# the colour, according to the gist_rainbow colormap.
# Data points are rendered as half transparent to allow
# data point overlap to be seen.
the_plot = ax.scatter(features[0], features[1], alpha=0.5,
            s=200*features[3], c=iris.target, cmap="gist_rainbow")
# Add a colormap to the plot.
fig.colorbar(the_plot)
# Set the Figure's title and axis labels.
ax.set_title("IRIS data set")
ax.set_xlabel(iris.feature_names[0])
ax.set_ylabel(iris.feature_names[1])
# Display the Figure
plt.show()