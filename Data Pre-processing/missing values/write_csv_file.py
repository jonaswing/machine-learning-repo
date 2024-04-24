# header:  A list of entries to serve as the column headers for the file
# data:  A list containing the data to write to file
# file_name:  The name of the file to create
def write_csv_file(header, data, IRISa):
    # Opens the file for writing
    my_file = open(IRISa, "w")
    # Writes the header to file as a comma-separated string
    my_file.write("{}\n".format(",".join(header)))
    # Iterates through the various entries in the data list
    for line in data:
        # Writes each entry in the list to file as a comma-separated string
        my_file.write("{}\n".format(",".join(line)))
    # Closes the file to release the resource
    my_file.close()