# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Determines the unique occurences species column, along with the number of occurences of each
print(df["species"].value_counts())