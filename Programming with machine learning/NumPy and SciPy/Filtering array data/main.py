# Import numpy with the alias np
import numpy as np

# Create data set filled with random numbers in the range 0 to 100
data = np.random.randint(100,size=(3, 3))
# Create a boolean list to serve as the filter
filter = [True, False, True]

data_filtered_by_row = data[filter]
data_filtered_by_column = data[:,filter]
# Display the original and filtered data
print("Original:\n", data)
print("\nFiltered by row:\n", data_filtered_by_row)
print("\nFiltered by column:\n", data_filtered_by_column)