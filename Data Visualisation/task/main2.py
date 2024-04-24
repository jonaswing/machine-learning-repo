import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(0)

data1 = np.random.uniform(40, 100, 50)
data2 = np.random.uniform(10, 200, 80)
data3 = np.random.uniform(120, 180, 90)
data4 = np.random.uniform(80, 160, 60)

data = [data1, data2, data3, data4]

# Custom whisker lengths
whiskerprops = dict(linestyle='--', linewidth=1.5, color='blue')

# Create boxplot
plt.boxplot(data, vert=False, whis=[5, 95], whiskerprops=whiskerprops)

# Customize y-axis labels
plt.yticks([1, 2, 3, 4], ['Dataset 1', 'Dataset 2', 'Dataset 3', 'Dataset 4'])

# Customize x-axis labels
plt.xticks(np.arange(25, 201, 25))

# Add grid
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Add labels and title
plt.xlabel('Values')
plt.ylabel('Datasets')
plt.title('Horizontal Box and Whisker Plot')

# Show plot
plt.tight_layout()
plt.show()
