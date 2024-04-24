# import pandas under the alias pd
import math

import pandas as pd
# import sklearn.preprocessing under the alias pre
import sklearn.preprocessing as pre

# Create 3 columns of data each with 4 values.
data = [[9, 2, 7],
        [1, 5, 6],
        [1, 5, 1],
        [7, 8, 9]]

# Create a new DataFrame from the data assign names to the columns
demo = pd.DataFrame(data, columns=["Feature 1", "Feature 2", "Feature 3"])
# Display the contents of the DataFrame
print("Data set before normalisation:\n", demo)


# MAX NORMALISATION
# Performs max normalisation and stores the result
max_results = pre.normalize(demo, norm="max")
# Converts the result to a DataFrame
max_results = pd.DataFrame(max_results, columns=["Feature 1", "Feature 2", "Feature 3"])
# Output the results of performing l1 normalisation
print("\nData set after max normalisation:\n", max_results)


# L1 NORMALISATION
# Performs l1 normalisation and stores the result
l1_results = pre.normalize(demo, norm="l1")
# Converts the result to a DataFrame
l1_results = pd.DataFrame(l1_results, columns=["Feature 1", "Feature 2", "Feature 3"])
# Adds a total column.  The totals are calculated by summing the values in each row (axis=1).
l1_results["Total"] = l1_results.sum(axis=1)
# Output the results of performing l1 normalisation
print("\nData set after l1 normalisation:\n", l1_results)


# L2 NORMALISATION
# This function receives a single row at a time.
def calculate_l2_total(row):
        # Initialises a total variable
        total = 0
        # Iterates through each item in the row.
        for x in row:
                # Adds the square of the item to the running total.
                total += x ** 2
        # Returns the total.
        return total


# Performs l2 normalisation and stores the result
l2_results = pre.normalize(demo, norm="l2")
# Converts the result to a DataFrame
l2_results = pd.DataFrame(l2_results, columns=["Feature 1", "Feature 2", "Feature 3"])
# Adds a total column.  The totals are calculated by applying a custom function to each row (axis=1).
l2_results["Total"] = l2_results.apply(calculate_l2_total, axis=1)
# Output the results of performing l2 normalisation
print("\nData set after l2 normalisation:\n", l2_results)
