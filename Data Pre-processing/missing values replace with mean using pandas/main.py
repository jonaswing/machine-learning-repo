import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('IRISa.csv')

# Calculate the mean of each column and round to one decimal place
mean_values = df.mean().round(1)

# Replace missing values with the rounded mean of each column
df.fillna(mean_values, inplace=True)

# Save the DataFrame back to a CSV file
df.to_csv('IRISa_filled.csv', index=False)
