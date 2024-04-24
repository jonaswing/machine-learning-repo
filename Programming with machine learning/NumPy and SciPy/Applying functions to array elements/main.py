# Import numpy with the alias np
import numpy as np

# Create a two-dimensional array containing 9 values
data = np.arange(9).reshape(3,3)

# Add 10 to every element in the array
data_10 = data + 10
# Original data
print("Original data:\n", data)
# Output the modified array
print("10 added to every element:\n", data_10)