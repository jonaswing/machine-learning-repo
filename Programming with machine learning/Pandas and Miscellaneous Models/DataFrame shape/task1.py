import pandas as pd

# Load the existing CSV file into a Pandas DataFrame
df = pd.read_csv('excel_data.csv', index_col='participant_name', sep=";")

# Add at least 10 more rows with Python code
additional_data = {
    'participant_name': ['Participant11', 'Participant12', 'Participant13', 'Participant14', 'Participant15',
                         'Participant16', 'Participant17', 'Participant18', 'Participant19', 'Participant20'],
    'time_in_seconds': [35, 40, 42, 38, 41, 36, 39, 45, 37, 43]
}

# Convert the additional data to a DataFrame
additional_df = pd.DataFrame(additional_data)

# Concatenate the existing DataFrame with the additional data
df = pd.concat([df, additional_df.set_index('participant_name')])

# Save the updated DataFrame to a new CSV file
df.to_csv('excel_data_updated.csv')

# Display the Pandas Series
print(df['time_in_seconds'])
