import pandas as pd

# Read the CSV file
df = pd.read_csv('IRISa.csv')

# Replace missing values with the median of each column
df.fillna(df.median(), inplace=True)

# Save the updated data to a new CSV file
df.to_csv('IRISa_updated.csv', index=False)
