# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Displays the first 5 rows of the DataFrame
print("Head - Default first 5 rows")
print(df.head())
# Displays the first 3 rows of the DataFrame
print("\nHead - First 3 rows")
print(df.head(3))