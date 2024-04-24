import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


# Generate synthetic data
X, y = make_blobs(n_samples=100, centers=2, random_state=42)


# Separate data points into two arrays based on blobs
blob1_points = X[y == 0][:, 1]
blob2_points = X[y == 1][:, 1]


# Create box and whisker plots
plt.boxplot([blob1_points, blob2_points], whis=(20, 80))


# Display the Figure.
plt.show()





