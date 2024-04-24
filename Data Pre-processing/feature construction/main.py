def generate_output(data):
    # Output the values in the data set by processing each line (instance) in turn...
    for instance in data:
        # and then processing each value (feature) in the instance in turn.
        for feature in instance:
            print("{0:5}".format(feature), end="")
        # Adds a new line at the end of every line of output
        print()


def generate_data():
    # To store an example dataset with the following (pre-processed) features
    # branch_id
    # sales_item
    # year
    # month
    # male (number of customers making item purchase - gender demographics from loyalty program)
    # female (number of customers making item purchase - gender demographics from loyalty program)
    # non-binary (number of customers making item purchase - gender demographics from loyalty program)
    # weather_condition (various weather conditions were assigned numeric values via pre-processing)
    input_values = list()
    input_values.append([5, 345, 2020, 3, 23, 15, 3, 2])
    input_values.append([3, 374, 2021, 4, 56, 54, 52, 1])
    input_values.append([4, 123, 2019, 4, 82, 12, 25, 4])
    input_values.append([2, 786, 2020, 7, 59, 34, 10, 2])
    input_values.append([3, 837, 2018, 9, 91, 21, 28, 3])
    input_values.append([1, 543, 2020, 10, 3, 67, 18, 1])
    input_values.append([5, 123, 2018, 9, 12, 5, 4, 4])
    input_values.append([2, 883, 2019, 2, 8, 15, 3, 3])
    input_values.append([5, 901, 2021, 1, 55, 17, 8, 3])
    input_values.append([1, 453, 2020, 11, 178, 123, 87, 2])
    return input_values


# Call the generate_data() function to generate the data set.
data = generate_data()
# A header for the input values
print("{0}Input data{1}".format("-" * 20, "-" * 20))
# Call the generate_output function to output the data set to the console window.
generate_output(data)

# Process every attribute in turn
for i in range(0, len(data)):
    # Calculates a new feature for every instance by adding up the values for the features
    # male, female and non-binary
    new_feature = data[i][4] + data[i][5] + data[i][6]
    # Add the newly created feature to the end of the current instance
    data[i].append(new_feature)

# A header for the output values
print("\n{0}Output data{1}".format("-" * 20, "-" * 20))
# Call the generate_output function to output the data set to the console window.
generate_output(data)