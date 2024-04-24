# Import pandas with the alias pd
import pandas as pd

# Reads the target csv file and returns the contents in the form of a Pandas DataFrame
df = pd.read_csv("IRIS.csv")

# Displays the default results of calling the memory_usage method
print("Default:")
print(df.memory_usage())

# Displays the results of calling the memory_usage method,
# excluding the index and performing a deeper system-level calculation
print("\nDeep and without index:")
print(df.memory_usage(index=False, deep=True))