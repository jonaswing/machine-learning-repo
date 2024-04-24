# Import numpy with the alias np
import numpy as np

# Create a one-dimensional array of 100 values.
data = np.arange(100)

# Display the details of the initial array
print("Initial array:\n", data, "\nShape: ", data.shape)

# Change the array to 10 rows across 10 columns
data_reshaped = data.reshape(10, 10)

# Display the details of the reshaped array
print("\nReshaped array:\n", data_reshaped, "\nShape: ", data_reshaped.shape)