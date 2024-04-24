import numpy as np

# Create two arrays; one with arranged values and another filled
# with the same value for each element
data_arange = np.arange(9).reshape(3,3)
data_full = np.full((3,3), fill_value=10)
# Display the details of the two generated arrays
print("Sequential data:\n", data_arange)
print("\nFilled data:\n", data_full)
# Multiply arrays to create a new array
data_multiplied = data_arange * data_full
# Display the details of the multiplied arrays
print("\nMultiplied data:\n", data_multiplied)