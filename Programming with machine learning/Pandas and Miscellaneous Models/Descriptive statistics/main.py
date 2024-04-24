# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Display first 5 rows of the dataset
print(df.head())
print()

# Generate a DataFrame containing descriptive statistics for the Iris dataset
stats = df.describe()
# Display all the contents of the stats DataFrame
print(stats)