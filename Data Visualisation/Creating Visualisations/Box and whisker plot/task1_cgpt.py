import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Generate synthetic data
X, y = make_blobs(n_samples=500, centers=2, random_state=42)

# Separate data points into two arrays based on blobs
blob1_points = X[y == 0][:, 1]
blob2_points = X[y == 1][:, 1]

# Create box and whisker plots
plt.boxplot([blob1_points, blob2_points], widths=0.5, patch_artist=True,
            boxprops=dict(facecolor='skyblue', color='black'),
            whiskerprops=dict(color='black'), medianprops=dict(color='black'),
            flierprops=dict(marker='x', markersize=8, color='purple'))

# Set whiskers at 20th and 80th percentiles
plt.gca().set_ylim(bottom=np.percentile(np.concatenate((blob1_points, blob2_points)), 20),
                   top=np.percentile(np.concatenate((blob1_points, blob2_points)), 80))

plt.xticks([1, 2], ['Blob 1', 'Blob 2'])
plt.xlabel('Blobs')
plt.ylabel('Y-coordinate')

plt.show()
