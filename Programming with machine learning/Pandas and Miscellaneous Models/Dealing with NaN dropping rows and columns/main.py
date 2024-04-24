# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Output the original DataFrame shape
print("Original: ", df.shape)

# Outputs the shape of the DataFrame after dropping NaN values
print("Drop rows containing NaN: ", df.dropna().shape)
print("Drop columns containing NaN: ", df.dropna(axis=1).shape)
print("Drop rows containing NaN in column sepal_length: ", df.dropna(subset=["sepal_length"]).shape)