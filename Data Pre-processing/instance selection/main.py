from random import random


# data:  In a real-world environment, data would be used by a classifier or during a machine learning
# algorithm training/learning phase. This simulation can only improve or decrease accuracy by a maximum
# of 5% per call
def simulate_classification(data, previous_accuracy):
    # Returns a random value in the range 0 to 1.
    return previous_accuracy + (random() * .10) - .05


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


# data:  The full data set from which to generate the subset.
# threshold:  The accuracy threshold at which to stop creating the data subset.
def incremental(data, threshold):
    # Creates an empty list to serve as the data subset
    subset = list()
    # Creates a copy of the full data set to be able to remove entries when creating the subset
    data_copy = data.copy()
    # Sets the initial accuracy of the model for comparison purposes.
    accuracy = 0
    # Continue iterating until the accuracy has reached the required threshold and
    # while the copy of the main data set still has entries that have not been added
    # to the subset. The iterations field tracks how many times the subset was updated.
    iterations = 0
    while accuracy < threshold and len(data_copy) > 0:
        # Increments the number of iterations
        iterations += 1
        # Randomly generates an index in the copy of the full data set to make a selection from it.
        index = int(random() * len(data_copy))
        # Appends the randomly selected instance to the subset data set.
        subset.append(data_copy[index])
        # Generates the accuracy value associated with the subset
        temp_accuracy = simulate_classification(subset, accuracy)
        # If it does then remove the instance from the copy of the full data set, to ensure
        # than it is selected only once. And stores the current accuracy of the classifier for
        # future comparisons.
        if temp_accuracy > accuracy:
            accuracy = temp_accuracy
            # Displays the current accuracy (to demonstrate improvement)
            print("Current accuracy: ", accuracy)
            del(data_copy[index])
        else:
            # Otherwise, remove the extra instance from the subset, as it did not yield an improvement.
            subset.pop()

    # Displays the number of iterations completed.
    print("Iterations completed:  {0}".format(iterations))
    # Returns the subset data set
    return subset


def main():
    # Reads the data from the IRIS.csv file
    data = read_csv_file("IRISa.csv")
    # Displays how many entries there are in the full data set
    print("Full data set size:  {0} entries".format(len(data)))
    # Generates the subset data set with an 80% accuracy threshold
    subset = incremental(data, 0.8)
    # Displays how many entries there are in the subset data set
    print("Subset data set size:  {0} entries".format(len(subset)))