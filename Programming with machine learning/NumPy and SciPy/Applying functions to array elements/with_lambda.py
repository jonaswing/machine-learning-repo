# Import numpy with the alias np
import numpy as np

# Create a two-dimensional array containing 9 values
data = np.arange(9).reshape(3,3)

# Define an in-line function which squared each element in an input array
# and adds 50.
my_func = lambda arr: arr ** 2 + 50
# Apply the inline function to every element in the array to create a modified
# array
data_func = my_func(data)
# Output the modified array
print("Function applied to every element:\n", data_func)