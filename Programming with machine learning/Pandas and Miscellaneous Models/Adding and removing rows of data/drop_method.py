# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Demonstrating how to drop rows and columns
print("Drop a single row by index:\n", df.drop([2]).head(), end="\n\n")
print("Drop multiple rows by index:\n", df.drop([2, 3, 5]).head(), end="\n\n")
print("Drop a single column by name:\n", df.drop(columns=["sepal_length"]).head(), end="\n\n")
print("Drop a multiple columns by name and axis:\n", df.drop(["sepal_width", "petal_width"], axis=1).head(), end="\n\n")

print(df.drop([0,1,2], axis=0).head())
print(df.drop(columns=['sepal_width']).head())

