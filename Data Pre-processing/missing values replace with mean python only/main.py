# Read the CSV file and store the data in a list of lists
with open('IRISa.csv', 'r') as file:
    lines = file.readlines()

# Extract column names and data separately
column_names = lines[0].strip().split(',')
data = [line.strip().split(',') for line in lines[1:]]

# Function to calculate the mean of a column and round to one decimal place
def calculate_mean(column):
    values = [float(row[column]) for row in data if row[column].replace('.', '', 1).isdigit()]
    if values:
        return round(sum(values) / len(values), 1)
    else:
        return None

# Function to replace missing values with the mean of the column
def replace_missing_with_mean(column, mean):
    for row in data:
        if not row[column].replace('.', '', 1).isdigit():
            row[column] = str(mean)

# Calculate and replace missing values with the mean for each column
for col in range(len(data[0])):
    col_mean = calculate_mean(col)
    if col_mean is not None:
        replace_missing_with_mean(col, col_mean)

# Write the modified data back to a new CSV file with column names
with open('IRISa_filled.csv', 'w') as file:
    file.write(','.join(column_names) + '\n')
    for row in data:
        file.write(','.join(row) + '\n')

print("Output:")
print("\nLines in data:", len(data) + 1)  # +1 to include the header

# Display column names
for col in column_names:
    print(f'{col:15}', end='')
print()

# Display data
for i, row in enumerate(data):
    if i < 10 or i >= len(data) - 10:
        for val in row:
            print(f'{val:15}', end='')
        print()
    elif i == 10:
        print("\n140 lines omitted\n")