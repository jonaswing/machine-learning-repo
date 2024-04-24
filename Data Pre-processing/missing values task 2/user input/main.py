import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('IRISa.csv')

# Prompt the user for the value to replace missing values
replacement_value = float(input("Enter the value to replace missing values: "))

# Replace missing values with the user-inputted value
df.fillna(replacement_value, inplace=True)

# Save the updated DataFrame to a new CSV file
df.to_csv('IRISa_updated.csv', index=False)

print("Missing values replaced and saved to IRISa_updated.csv.")
