import matplotlib.pyplot as plt
import numpy as np

# Generating random data
np.random.seed(0)  # For reproducibility

data1 = np.random.randint(40, 101, 50)
data2 = np.random.randint(10, 201, 80)
data3 = np.random.randint(120, 181, 90)
data4 = np.random.randint(80, 161, 60)

# Customizing whisker props
whiskerprops = dict(color='blue', linestyle='-', linewidth=1.5)

# Creating box and whisker plot
plt.figure(figsize=(10, 6))
plt.boxplot([data1, data2, data3, data4], vert=False, whis=[5, 95], whiskerprops=whiskerprops)

# Customizing labels
plt.yticks([1, 2, 3, 4], ['Dataset 1', 'Dataset 2', 'Dataset 3', 'Dataset 4'])
plt.xticks(np.arange(25, 201, 25))

# Adding grid
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Adding title and labels
plt.title('Horizontal Box and Whisker Plot')
plt.xlabel('Value')
plt.ylabel('Datasets')

# Showing the plot
plt.tight_layout()
plt.savefig('boxplot.jpg')  # Saving the plot as an image
plt.show()
