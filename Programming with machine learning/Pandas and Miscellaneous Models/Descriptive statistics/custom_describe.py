# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Display first 5 rows of the dataset
print(df.head())
print()

# Generate a DataFrame that includes all attributes, and replaces the 25th and 75th
# percentile with the 10th and 90th percentile
stats = df.describe(include="all", percentiles=[.1, .9])
# Display all the contents of the stats DataFrame
print(stats)