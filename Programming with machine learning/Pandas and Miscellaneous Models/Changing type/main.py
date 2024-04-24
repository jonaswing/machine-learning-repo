# Import pandas with the alias pd
import pandas as pd

data = {"height": [177, 154, 129, 192],
        "weight": [67, 58, 49, 102],
        "age": [55, 23, 10, 34]}

df = pd.DataFrame(data)

# Creates a copy of the DataFrame in which numeric values have been converted to float.
float_df = df.astype(dtype="float64")

# Displays only the first 5 rows of the modified DataFrame
print("Modified: \n", float_df.head(5))

# Displays only the first 5 rows of the original DataFrame,
# to demonstrate that it was not modified.
print("\nOriginal: \n", df.head(5))

# Creates a copy of the original DataFrame with the height and weight columns
# converted to float.
df_modified = df.astype({"height" : "float64", "weight" : "float64"})
# Use the DataFrame's dtypes property do display the data types of all the columns
print("\nModified data types:\n", df_modified.dtypes, sep="")