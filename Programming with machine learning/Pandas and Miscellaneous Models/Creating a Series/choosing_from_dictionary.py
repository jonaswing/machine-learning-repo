# Import pandas with the alias pd
import pandas as pd

# Declare a list of values
the_dict = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7}

# Use the full dictionary to initialise a Pandas Series
the_series_one = pd.Series(the_dict)
# Use a subset of the dictionary to initialise a Pandas Series
the_series_two = pd.Series(the_dict, index = [ "a", "c", "e", "g"])

# Display the contents of both series
print("Full:")
print(the_series_one)
print("Partial:")
print(the_series_two)