# Import numpy with the alias np
import numpy as np

# Generate a one-dimensional array
# filled with 10 random integers in the range 0 to 100
data = np.random.randint(19,22, size=(10))

# Display the details of the original data
print("Array:\n", data)
# Display the matching indices after performing a search
print("\nIndices of elements equal to 20: ", np.where(data == 20))
print("\nIndices of elements greater than 20: ", np.where(data > 20))
print("\nIndices of elements which are uneven: ", np.where(data % 2 == 1))