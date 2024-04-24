from calculate_distance import calculate_distance
from check_for_missing import check_for_missing


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

contents = read_csv_file("setosa.csv")

header = contents[0]

data = contents[1:]

write_csv_file(header, data, "updated_setosa.csv")










