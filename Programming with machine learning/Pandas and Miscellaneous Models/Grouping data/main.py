# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Output the mean of petal_length for each of the unique species, according to the species column
print(df.groupby(by="species").petal_length.mean())