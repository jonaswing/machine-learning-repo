import display_data, read_csv_file, write_csv_file


def main():
    # Calls the read_csv_file function to read the contents
    # of the IRIS.csv file and return it as a list of lists.
    contents = read_csv_file(my_file)
    # Creates a slice of the list that stores only the header of the IRIS.csv file.
    header = contents[0]
    # Creates a slice of the list that stores all the data tuples of the IRIS.csv file.
    data = contents[1:]
    # Functions for dealing with missing values will be called between the START and END lines.
    # START
    
    # END
    # Uses the display_data function to display the first 10 tuples
    display_data(header, data, 10)
    # Writes the (modified) data set back to file.
    write_csv_file(header, data, "IRIS updated.csv")

# This is the starting point of the program.
if __name__ == "__main__":
    # When the program starts, the main function is called.
    main()