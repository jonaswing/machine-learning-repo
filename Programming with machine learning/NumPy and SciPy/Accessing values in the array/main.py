# Import numpy with the alias np
import numpy as np

# Create a two-dimensional array containing 9 values
data = np.arange(9).reshape(3,3)

# Display the details of the initial array
print("Initial array:\n", data, "\nShape: ", data.shape)

# Display the data from a specific location in the array
print("Data at index 2, 2: ", data[1,1])
# Modifying data at a specific index
data[1, 1] = 99
print("Data at index 2, 2: ", data[1,1])
# Modifying values in an array by processing them via a loop.
# The shape array contains the size of each dimension, which may be used
# to control the number of iterations for looping through the elements in
# each dimension.
for row in range(0, data.shape[0]):
    for column in range(0, data.shape[1]):
        data[row, column] = data[row, column] + 1

# Display the details of the initial array
print("Updated array:\n", data, "\nShape: ", data.shape)
