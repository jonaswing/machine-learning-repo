import math


# first:  The first tuple to be used in the distance calculation. Passed as a list.
# second:  The second tuple to be used in the distance calculation. Passed as a list.
def calculate_distance(first, second):
    # Sets a variable to use for the running total of the attribute difference squares.
    total = 0
    # Use zip to iterate over both tuples at the same time.
    for a, b in zip(first, second):
        # Checks to make sure that neither attribute has a missing value.
        if a.strip() != "" and b.strip() != "":
            # If not, calculate the difference between the two attribute values, square it and add it to the running total.
            total += math.pow(a - b, 2)

    # Calculate the square root of the running total and return it as the calculated distance.
    return math.sqrt(total)