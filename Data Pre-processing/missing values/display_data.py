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