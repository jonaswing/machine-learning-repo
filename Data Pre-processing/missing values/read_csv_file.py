import os

# file_name:  represents the name of the file to import
def read_csv_file(file_name="IRIS.csv"):
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