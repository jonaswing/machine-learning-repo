import numpy as np

# Create data set filled with random numbers in the range 0 to 100
data = np.random.randint(100,size=(3, 3))
# Display the original data
print("Original:\n", data)
# Create an array to serve as a filter.  The array will contain a
# True or False value as to whether each element in the array is
# greater than 20
filter_1 = data > 20
# Create another array to serve as a filter.  The array will contain a
# True or False value as to whether each element in the array is
# fully divisible by 2.  This has the effect of only returning even numbers.
filter_2 = data % 2 == 0

# Display the data resulting from applying the two filters
print("\nFiltered to only return values greater than 20:\n", data[filter_1])
print("\nFiltered to only return even numbers:\n", data[filter_2])