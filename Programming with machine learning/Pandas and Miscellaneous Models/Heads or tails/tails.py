# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Displays the first 5 rows of the DataFrame
print("Tail - Default last 5 rows")
print(df.tail())
# Displays the first 3 rows of the DataFrame
print("\nTail - Last 3 rows")
print(df.tail(3))