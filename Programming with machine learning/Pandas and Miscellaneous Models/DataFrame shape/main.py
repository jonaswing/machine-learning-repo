# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Outputs the contents of the DataFrame
print("Contents:\n", df)

# Outputs the shape details of the DataFrame
print("\nShape: ", df.shape)