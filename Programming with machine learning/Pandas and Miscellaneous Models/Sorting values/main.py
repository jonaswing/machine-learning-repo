# Import pandas with the alias pd
import pandas as pd

data_1 = { "id": [27, 46, 12, 54, 31],
        "height": [177, 154, 129, 166 ,192],
        "weight": [67, 58, 49, 80, 102],
        "age": [55, 23, 10, 34, 72]}

data_2 = { "id": [99, 123, 157],
        "height": [112, 189, 156],
        "weight": [45, 97, 65],
        "age": [10, 55, 46]}

# Create 2 DataFrames from the provided data
df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)

# Create a combined DataFrame
combined = df_1.append(df_2)

# Outputs the original DataFrame
print("Original:\n", combined, end="\n\n")
# Outputs the result of sorting the DataFrame on age
print("Sorted on age:\n", combined.sort_values(by=["age"]), end="\n\n")
# Outputs the result of sorting the DataFrame on age and then on height
print("Sorted on age and height:\n", combined.sort_values(by=["age", "height"]))