# Import numpy with the alias np
import numpy as np

# Create an array filled with random numbers in the range 0 to 1.
data_1 = np.random.rand(5, 5)
# Create an array filled with random integers between 0 and the maximum value specified.
data_2 = np.random.randint(100, size=[5, 5])

# Display the contents of the 2 arrays
print("data_1:\n", data_1)
print("\ndata_2:\n", data_2)