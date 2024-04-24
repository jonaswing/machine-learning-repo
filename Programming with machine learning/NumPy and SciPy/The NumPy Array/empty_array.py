# Import numpy with the alias np
import numpy as np

# Create 3 different empty numpy arrays by providing a shape
data_1 = np.empty([5, ])
data_2 = np.empty([10, 5], dtype=int)
data_3 = np.empty([5, 10, 5], dtype=float)

# Print the details of the 3 arrays
print("data_1 Shape: ", data_1.shape)
print("data_2 Shape: ", data_2.shape)
print("data_3 Shape: ", data_3.shape)

print("data_1 Contents: ", data_1)