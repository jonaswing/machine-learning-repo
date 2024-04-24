# Import pandas with the alias pd
import pandas as pd

# Create a dictionary with a key, to be used as a label, and a list as the value.
data = {"height": [177, 154, 129, 192],
        "weight": [67, 58, 49, 102],
        "age": [55, 23, 10, 34]}


# Creates a DataFrame with 3 columns; "height”, "weight" and “age”.  The column names are taken from the
# keys of the dictionary and the values in the column are taken from the associated lists.
df = pd.DataFrame(data)


print("Rows where age is equal to 23:\n", df.loc[df.age == 23], "\n")
print("Rows where weight is greater than 50:\n", df.loc[df.weight > 50], "\n")
print("Rows where height is less than or equal to 150:\n", df.loc[df.height <= 150], "\n")