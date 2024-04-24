import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Create 200 samples, each consisting of 3 features
# spread across 3 centers. The data points have
# standard deviation of 2 and the values are generated
# using a random_state of 37 for the sake of consistency.
X, y = make_blobs(200, n_features=3,
                  centers=3, cluster_std=2,
                  random_state=37)

plt.rcParams.update({"font.size": 22, "figure.figsize": [19.20, 10.80]})

# Create a Figure.
fig = plt.figure()
# Create a new Axes object associated with the current figure.
# Setting the projection to 3d, creates a 3D plot.
ax = plt.axes(projection ='3d')
# Set the elevation angle of the 3D view to 10 degrees
# and the azimuth angle of the x, y plane to 10 degrees.
ax.view_init(10, 10)
# Plot 3 different scatter plots. One for each blob.
colors = ["blue", "green", "purple"]
# Iterate over the 3 different colours.
for k, col in enumerate(colors):
    # Create a map of values of cases where the index of the
    # colour is equal to the blob index in y from the
    # make_blobs() function.
    cluster_data = y == k
    # Plots only the data points which fall into the specific
    # blob. The data points are plotted in the associated colour
    # at a size of 100.
    ax.scatter3D(X[cluster_data, 0],
                 X[cluster_data, 1],
                 X[cluster_data, 2],
                 c=col,
                 label=col,
                 s=100)

# Add a legend to the Axes.
ax.legend()
# Display the plot.
plt.show()