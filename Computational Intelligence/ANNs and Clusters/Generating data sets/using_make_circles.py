from sklearn.datasets import make_circles
from pandas import DataFrame
import matplotlib.pyplot as plt


X, y = make_circles(n_samples=250, noise=0.1)


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




