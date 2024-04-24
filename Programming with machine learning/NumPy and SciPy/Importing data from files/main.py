import numpy as np

# Specify that all data be read as object
data_1 = np.genfromtxt("IRIS.csv", delimiter=",", dtype=object, max_rows=5)

# Load the data, but skip the header column and selectively replace
# missing values
data_2 = np.genfromtxt("IRIS.csv",
                       delimiter=",",
                       skip_header=1,
                       dtype=(float, float, float, float, object),
                       filling_values=(0,0, 0.0, 0.0, 0.0, "Not provided"),
                       max_rows=5)

# Display the results of reading all values as object
print(data_1)
print()
# Display the results of reading columns as specific data types
print(data_2)
