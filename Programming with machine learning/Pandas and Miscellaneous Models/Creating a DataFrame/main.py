# Import pandas with the alias pd
import pandas as pd

# Create a dictionary with a key, to be used as a label, and a list as the value.
data = {"height": [177, 154, 129, 192],
        "weight": [67, 58, 49, 102],
        "age": [55, 23, 10, 34]}


# Creates a DataFrame with 3 columns; "height”, "weight" and “age”.  The column names are taken from the
# keys of the dictionary and the values in the column are taken from the associated lists.
df = pd.DataFrame(data)

# Display the contents of the DataFrame
print(df)


# Display all the rows starting from index 2
print(df[2:])
# Display the rows from index 0 to index 2
print(df[0:2])
# Display every second row from index 0 to index 3
print(df[0:3:2])


# Print the row at index 1
print("Index 1:\n", df.loc[1], "\n")
# Print the rows at indexes 1 and 3
print("Index 1 and 3:\n", df.loc[[1,3]], "\n")
# Print the rows at indexes 1 to 3
print("Index 1 to 3:\n", df.loc[1:3], "\n")