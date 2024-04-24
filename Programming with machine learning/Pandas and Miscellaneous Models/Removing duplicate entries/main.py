# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Displays the statistics of the dataset before removing duplicates
print("Before removing duplicates:\n", df.describe(), sep="")

# Keeps only the first of each duplicate and makes a copy of the updated dataset
df.drop_duplicates(keep="first", inplace=True)

# Displays the statistics of the dataset after removing duplicates
print("\nAfter removing duplicates:\n", df.describe(), sep="")

# The dataset now has fewer count of each column, because we removed duplicates
