# Import pandas with the alias pd
import pandas as pd

# Create a dictionary with a key, to be used as a label, and a list as the value.
data = {"height": [177, 154, 129, 192],
        "weight": [67, 58, 49, 102],
        "age": [55, 23, 10, 34]}


# Creates a DataFrame with 3 columns; "height”, "weight" and “age”.  The column names are taken from the
# keys of the dictionary and the values in the column are taken from the associated lists.
df = pd.DataFrame(data)


# Print the rows at indexes 1 to 3, but only for the columns "height" and "age"
print("Index 1 to 3, height and age:\n", df.loc[1:3, ["height", "age"]], "\n")