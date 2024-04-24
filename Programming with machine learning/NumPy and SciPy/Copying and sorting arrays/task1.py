import numpy as np

# Random numbers from 0 to 1
data = np.random.rand(100).reshape(10, 10).round(3)

# Copying the data, then sorting it
copy_data = np.copy(data)

# The numbers are sorted in each row
copy_data = np.sort(copy_data)

# The original data
print("Original data: \n", data, "\n")

# The copied and sorted data
print("Copied and sorted data: \n", copy_data, "\n")

