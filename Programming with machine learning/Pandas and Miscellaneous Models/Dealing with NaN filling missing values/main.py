# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Demonstrates how to use fillna()
print("Original:\n", df.head(), end="\n\n", sep="")
print("Fill all NaN values with the value 0:\n", df.fillna(0).head(), end="\n\n", sep="")
sepal_length_mean = df["sepal_length"].mean()
print("Fill all NaN values in sepal_length with the column mean:\n",
      df["sepal_length"].fillna(sepal_length_mean).head(), end="\n\n", sep="")