import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('IRISa.csv')

# Replace missing values with the mode of each column
df = df.apply(lambda x: x.fillna(x.mode()[0]))

# Save the updated DataFrame to a new CSV file
df.to_csv('IRISa_updated.csv', index=False)
