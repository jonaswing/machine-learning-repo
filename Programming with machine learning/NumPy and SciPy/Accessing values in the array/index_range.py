# Import numpy with the alias np
import numpy as np

# Create an array filled with the numbers 0 to 99, spread
# across 10 rows and columns
data = np.arange(100).reshape(10, 10)

# Retrieve only the first 3 rows and all columns
print("First 3 rows and all columns:\n", data[0:3])
# Retrieve all rows only the first 3 columns
print("\nFirst 3 columns and all rows:\n", data[:,0:3])
# Retrieve the first 3 rows and the first 3 columns
print("\nFirst 3 columns and first 3 rows:\n", data[0:3, 0:3])