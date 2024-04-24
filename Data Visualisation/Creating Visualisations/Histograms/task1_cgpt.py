import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
data = iris.data
feature_names = iris.feature_names

# Select sepal length feature
sepal_length = data[:, 0]

# Analyze (view) the values of sepal length
print("Sepal Length values:")
print(sepal_length)

# Determine bin ranges
bin_ranges = [4, 5, 6, 7, 8]

# Generate histogram
plt.figure(figsize=(8, 5))
plt.hist(sepal_length, bins=bin_ranges, orientation='horizontal')
plt.xlabel('Frequency')
plt.ylabel('Sepal Length')
plt.title('Histogram of Sepal Length')
plt.yticks(np.arange(4, 9), ['< 5', '5 - 6', '6 - 7', '7 - 8', '> 8'])
plt.grid(axis='x')
plt.show()
