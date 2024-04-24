import math


# file_name:  represents the name of the file to import
def read_csv_file(file_name):
    # Declare a list in which to store the individual lines of the file
    return_me = list()
    # Opens the file for reading
    my_file = open(file_name, "r")
    # Iterates through each line in the file
    for line in my_file:
        # Modifies the line to remove any linebreaks
        current = line.replace("\n","")
        # Split the individual entries in the line into a list
        # Adds the list to the return_me list
        return_me.append(current.split(','))

    # Closes the file to release the resource
    my_file.close()
    # Returns the list of values read from the file
    return return_me


# header:  A list of entries to serve as the column headers for the file
# data:  A list containing the data to write to file
# file_name:  The name of the file to create
def write_csv_file(header, data, file_name):
    # Opens the file for writing
    my_file = open(file_name, "w")
    # Writes the header to file as a comma-separated string
    my_file.write("{}\n".format(",".join(header)))
    # Iterates through the various entries in the data list
    for line in data:
        # Writes each entry in the list to file as a comma-separated string
        my_file.write("{}\n".format(",".join(line)))
    # Closes the file to release the resource
    my_file.close()


# first:  The first tuple to be used in the distance calculation. Passed as a list.
# second:  The second tuple to be used in the distance calculation. Passed as a list.
def calculate_distance(first, second):
    # Sets a variable to use for the running total of the attribute difference squares.
    total = 0
    # Use zip to iterate over both tuples at the same time.
    for a, b in zip(first, second):
        # Checks to make sure that neither attribute has a missing value.
        if a.strip() != "" and b.strip() != "":
            # If not, calculate the difference between the two attribute values,
            # square it and add it to the running total.
            total += math.pow(a - b, 2)

    # Calculate the square root of the running total and return it as the calculated distance.
    return math.sqrt(total)


# tuple:  The tuple to check for missing values
def check_for_missing(mytuple):
    # A flag that assumes there are no missing values
    missing = False
    # Iterates through all the values in the tuple
    for current in mytuple:
        # Tests for a missing value
        if current.strip() == "":
            # If a value is missing, set the flag to True
            missing = True
    # Returns the flag value
    return missing


# A class for tracking a data point (tuple) and its associated distance
class DataPoint:
    # A constructor that receives the tuple and distance and stores them
    def __init__(self, mytuple, distance):
        self.mytuple = mytuple
        self.distance = distance


# target:  The tuple for which to find neighbours.
# data:  The data set in which to find neighbours.
# k_value:  The number of neighbours to find.
def find_neighbours(target, data, k_value):
    # Defines a list of neighbours.
    neighbours = list()
    # Defines a list in which to store DataPoint objects
    data_with_distances = list()

    # Iterates through all of the items in the data set
    for current in data:
        # Performs a test to determine that the current tuple is not the current target and if its
        # not, that it doesn't contain missing values.
        if current != target and check_for_missing(current) == False:
            # Calculate the distance between this data point and the target tuple
            # and then appends it as a DataPoint to data_with_distances
            data_with_distances.append(DataPoint(current, calculate_distance(target, current)))

    # A loop that continues until the required number of neighbours have been found.
    while len(neighbours) < k_value:
        # Sets the minimum value to a high value so that all the other distances will be lower than this.
        min = 10000
        # An index used to keep track of the data item to set as a neighbour.
        index = -1
        # Iterates through all the items in the data_with_distances list.
        for i in range(0, len(data_with_distances)):
            # Test if the current item has a lower distance than the current lowest distance.
            if data_with_distances[i].distance < min:
                # If so, set this distance as the new minimum and save the index where this item may be found.
                min = data_with_distances[i].distance
                index = i

        # Add the data point with the lowest distance as a neighbour.
        neighbours.append(data_with_distances[index].mytuple)
        # Remove this data point from data_with_distances to ensure it is not selected again.
        data_with_distances.pop(index)

    # Return the list of neighbours.
    return neighbours


# data:  A list of neighbours from which to generate an average tuple.
def generate_average_tuple(data):
    # Creates an empty list in which to store the average tuple
    return_me = list()

    # Initialises the average tuple with 0 values for each attribute
    for i in range(0, len(data[0])):
        return_me.append(0)

    # Iterate through all the items in the list.
    for current in data:
        # For each neighbour, add the neighbour's attribute values to the average tuple's associated attribute
        for i in range(0, len(current)):
            return_me[i] += float(current[i])

    # Find the average of each attribute in the average_tuple by dividing each of its attribute values by
    # the number of neighbours.
    for i in range(0, len(return_me)):
        return_me[i] = return_me[i] / len(data)

    # Return the average tuple.
    return return_me


# data:  The data set in which to impute missing values.
# k_value:  The number of neighbours to find.
# decimal_digits:  The number of digits to which the mean should be rounded. Defaults to 1.
def impute_missing_values(data, k_value, decimal_digits=1):
    # Iterates through all of the items in the data set.
    for i in range(0, len(data)):
        # Checks if the current item has missing values.
        if check_for_missing(data[i]):
            # If so, find it's k closest neighbours.
            neighbours = find_neighbours(data[i],data, k_value)
            # Calculate the average tuple from those neighbours
            average_tuple = generate_average_tuple(neighbours)
            # Iterate through all of the attributes of the current tuple.
            for j in range(0, len(data[i])):
                # Tests if a specific attribute is missing.
                if data[i][j].strip() == "":
                    # If so, replace it with the associated attribute value from the average tuple.
                    format_string = "{0:." + str(decimal_digits) + "f}"
                    data[i][j] = format_string.format(float(average_tuple[j]))


def main():
    # Calls the read_csv_file function to read the contents
    # of the setosa.csv file and return it as a list of lists.
    contents = read_csv_file("setosa.csv")
    # Creates a slice of the list that stores only the header of the IRIS.csv file.
    header = contents[0]
    # Creates a slice of the list that stores all the data tuples of the IRIS.csv file.
    data = contents[1:]
    # Impute the missing values for data, 3 neighbouring data points.
    impute_missing_values(data, 3)
    # Writes the (modified) data set back to file.
    write_csv_file(header, data, "setosa_updated.csv")