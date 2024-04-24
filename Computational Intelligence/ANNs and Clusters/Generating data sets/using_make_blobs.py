from sklearn.datasets import make_blobs
from pandas import DataFrame
import matplotlib.pyplot as plt


# Generate 250 samples, as 4 clusters.  Each sample consists of 2 features.
X, y = make_blobs(n_samples=250, centers=4, n_features=2)


# Load the data into a DataFrame.
data_set = DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
print(data_set.head())


# Plot the data points
plt.figure(figsize=(8, 6))
plt.scatter(data_set['x'], data_set['y'], c=data_set['label'], cmap='viridis')

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Data')

# Show the plot
plt.colorbar(label='Label')
plt.show()


