# Import numpy with the alias np
import numpy as np

# Declare three separate numpy arrays using different approaches
arr_from_list = np.array([78, 232, 534, 123, 667, 34, 15])
arr_from_tuple = np.array((78, 232, 534, 123, 667, 34, 15))

# Output the results from creating arrays from different
# data sources; as well as the type of the object created.
print("From list: ", arr_from_list, "Type: ", type(arr_from_list))
print("From tuple: ", arr_from_tuple, "Type: ", type(arr_from_list))


# ////////////


data = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]]

# Declare three separate numpy arrays using different approaches
arr_data = np.array(data)

# Output the results from creating arrays from different
# data sources; as well as the type of the object created.
print("From multi-dimensional List:\n", arr_data, "\nType: ", type(arr_data))