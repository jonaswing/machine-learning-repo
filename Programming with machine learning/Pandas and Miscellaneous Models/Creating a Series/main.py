# Import pandas with the alias pd
import pandas as pd

# Declare a list of values
the_list = [1, 2, 3, 4, 5, 6, 7]

# Use the list to initialise a Pandas Series
the_series = pd.Series(the_list)

# Display the contents of the list
print("The list:")
print(the_list)

# Display the contents of the series
print("The series:")
print(the_series)