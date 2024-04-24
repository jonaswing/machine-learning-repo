# Import numpy with the alias np
import numpy as np

# Generate a two-dimensional 3, 3 array
# filled with random integers in the range 0 to 100
data = np.random.randint(100, size=(3, 3))

# Create a copy of the data set and sort it
data_copy = data.copy()
data_copy = np.sort(data_copy)

# Display the details of the original and copied data
print("Original:\n", data)
print("\nCopied and sorted:\n", data_copy)