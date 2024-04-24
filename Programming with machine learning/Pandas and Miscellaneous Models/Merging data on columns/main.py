# Import pandas with the alias pd
import pandas as pd

data_1 = { "id": [27, 46, 12, 54, 31],
        "height": [177, 154, 129, 166 ,192],
        "weight": [67, 58, 49, 80, 102]}

data_2 = { "id": [27, 46, 12, 31, 99],
        "age": [55, 23, 10, 34, 72]}

# Create 2 DataFrames from the provided data
df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)

# Outputs the original data
print(df_1, end="\n\n")
print(df_2, end="\n\n")

# Outputs the result of each type of merge on id
# when using df_1 as left and df_2 as right
print("left:\n", df_1.merge(df_2, on="id", how="left"), end="\n\n")
print("right:\n", df_1.merge(df_2, on="id", how="right"), end="\n\n")
print("outer:\n", df_1.merge(df_2, on="id", how="outer"), end="\n\n")
print("inner:\n", df_1.merge(df_2, on="id", how="inner"), end="\n\n")