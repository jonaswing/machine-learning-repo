# target:  A list of data from which to extract a column of data.
# column_index:  The index of the column in the data set to extract.
# ignore_first:  Indicates whether the first row of data should be ignored.
#  The default value is False. Set to True if the data contains headers.
def extract_column(data, column_index, ignore_first=False):
    # A temporary variable to store the values from the specific
    # column in the data set as a list
    return_me = list()
    # Specifies the default range of (all) data values to display
    range_values = range(0, len(data))
    # Overrides the default range, to start at the second row
    if ignore_first:
        range_values = range(1, len(data))
    # Iterates through all of the lines of data
    for current in range_values:
        # Selects the specified column's value from the current line of data
        # and appends it to the return_me list.
        return_me.append(data[current][column_index])
    
    # Returns the list of values that represents the column
    # from the data set.
    return return_me