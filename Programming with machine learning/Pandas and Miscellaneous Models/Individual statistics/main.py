# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Demonstrating various statistical calculations for the sepal_length column
print("sepal_length median: ", df["sepal_length"].median())
print("sepal_length mean: ", df["sepal_length"].mean())
print("sepal_length standard deviation: ", df["sepal_length"].std())
print("sepal_length minimum value: ", df["sepal_length"].min())
print("sepal_length maximum value: ", df["sepal_length"].max())
print("sepal_length sum: ", df["sepal_length"].sum())