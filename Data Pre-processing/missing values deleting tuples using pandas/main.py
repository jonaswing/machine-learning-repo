import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('IRISa.csv')

# Drop rows with missing values
df_cleaned = df.dropna()

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_IRISa.csv', index=False)

