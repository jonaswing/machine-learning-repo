# file_name:  represents the name of the file to import
def read_csv_file(file_name):
    # Declare a list in which to store the individual lines of the file
    return_me = list()
    # Opens the file for reading
    my_file = open(file_name, "r")
    # Iterates through each line in the file
    for line in my_file:
        # Modifies the line to remove any linebreaks
        current = line.replace("\n", "")
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

    # header:  A list of entries to serve as the column headers
    # data:  A list containing the data to display
    # lines:  The number of lines of data to display from a file. Can be left
    # at a default value of 0 to display all data.
    def display_data(header, data, lines=0):
        # Displays the total number of data entries
        print("Lines in data: {0}\n".format(len(data)))
        # Specifies the default range of (all) data values to display
        range_values = range(0, len(data))
        # Overrides the default range, using the number of lines
        # to display specified
        if lines > 0:
            range_values = range(0, lines)
        # Iterates through each value in the header and displays the
        # value centered in a 15-character space.
        for current in header:
            print("{0:^15}".format(current), end="")
        print()

        # Iterates through all of the lines of data
        for line in range_values:
            # Iterates through each value in the line and displays the
            # value centered in a 15-character space.
            for current in data[line]:
                print("{0:^15}".format(current), end="")
            print()
        # Displays a message stating how many entries were not displayed.
        if lines > 0:
            print("\n{} lines omitted".format(len(data) - lines))


# data:  A list containing data to process.
def remove_missing_rows(data):
    # Creates a list in which to store the new version of the data list.
    return_me = list()
    # Iterates through all of the lines of data.
    for line in data:
        # Sets an initial flag that assumes a tuple (line) has no missing values.
        add_me = True
        # Iterates through all the values in a tuple (line)
        for current in line:
            # Tests if an entry represents a missing value.
            if current.strip() == "":
                # Sets the flag to False if this is a missing value.
                add_me = False
        # If the tuple does not contain a missing value, add the entry
        # to the return_me list.
        if add_me:
            return_me.append(line)
    # Returns the updated data set (list)
    return return_me


def main():
    contents = read_csv_file("IRIS.csv")
    header = contents[0]
    data = contents[1:]
    # Calls the remove_missing_rows function
    data = remove_missing_rows(data)
    display_data(header, data, 10)
    write_csv_file(header, data, "IRIS updated.csv")