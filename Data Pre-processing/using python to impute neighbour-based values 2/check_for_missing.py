# tuple:  The tuple to check for missing values
def check_for_missing(tuple):
    # A flag that assumes there are no missing values
    missing = False
    # Iterates through all the values in the tuple
    for current in tuple:
        # Tests for a missing value
        if current.strip() == "":
            # If a value is missing, set the flag to True
            missing = True
    # Returns the flag value
    return missing