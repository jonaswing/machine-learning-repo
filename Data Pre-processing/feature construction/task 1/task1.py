def generate_output(data):
    for instance in data:
        for feature in instance:
            print("{0:5}".format(feature), end="")
        print()

def generate_data():
    input_values = list()
    input_values.append([5, 345, 2020, 3, 23, 15, 3, 2])
    # ... (the rest of the input values)

    return input_values

def calculate_percentage(data):
    total_male = sum(instance[4] for instance in data)
    total_female = sum(instance[5] for instance in data)
    total_non_binary = sum(instance[6] for instance in data)

    for i in range(len(data)):
        # Calculate percentages and scale to values between 0 and 1
        percentage_male = data[i][4] / total_male
        percentage_female = data[i][5] / total_female
        percentage_non_binary = data[i][6] / total_non_binary

        # Add the newly created features to the end of the current instance
        data[i].extend([percentage_male, percentage_female, percentage_non_binary])

# Call the generate_data() function to generate the data set.
data = generate_data()

# A header for the input values
print("{0}Input data{1}".format("-" * 20, "-" * 20))
# Call the generate_output function to output the data set to the console window.
generate_output(data)

# Process every attribute in turn
for i in range(0, len(data)):
    # Calculates a new feature for every instance by adding up the values for the features
    # male, female, and non-binary
    new_feature = data[i][4] + data[i][5] + data[i][6]
    # Add the newly created feature to the end of the current instance
    data[i].append(new_feature)

# A header for the output values
print("\n{0}Output data{1}".format("-" * 20, "-" * 20))

# Calculate and add three new features expressing each gender type as a percentage
calculate_percentage(data)

# Call the generate_output function to output the data set to the console window.
generate_output(data)
