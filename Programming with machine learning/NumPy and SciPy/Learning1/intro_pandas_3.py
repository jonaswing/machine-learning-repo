import pandas as pd

# Creating a DataFrame with both row and column indices
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data, index=['X', 'Y', 'Z'])

# Using direct indexing to select a column
result_direct_column = df['B']
print(result_direct_column)


# Using direct indexing to select a row
result_direct_row = df.loc['Y']
print(result_direct_row)


# Using iloc to select a column by integer position
result_iloc_column = df.iloc[:, 1]
print(result_iloc_column)


# Using iloc to select a row by integer position
result_iloc_row = df.iloc[1, :]
print(result_iloc_row)


