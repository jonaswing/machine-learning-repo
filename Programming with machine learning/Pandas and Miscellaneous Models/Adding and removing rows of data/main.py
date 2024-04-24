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

df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)

# Outputs the original data
print(df_1, end="\n\n")
print(df_2, end="\n\n")

# Outputs the result of appending the second DataFrame to the first.
combined = df_1.append(df_2)
print("Append: \n", combined, "\n")

# Append method will be deprecated, use concat method instead
combined_2 = pd.concat([df_1, df_2], ignore_index=True)
print("Concat: \n", combined_2)