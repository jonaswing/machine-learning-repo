# Import pandas with the alias pd
import pandas as pd

data = {"birth_date": ["23 October 1987", "15 July 1992", "9 February 1965"],
        "events" : [10, 3, 27]}

df = pd.DataFrame(data)

# Display the data types of the 2 columns of the DataFrame
print("Original:\n", df.dtypes, sep="")

# Convert the birth_date column to datetime using the to_datetime method and then
# reassigns it to the DataFrame's birth_date column
df["birth_date"] = pd.to_datetime(df["birth_date"])

# Display the data types of the 2 columns of the DataFrame after conversion
print("\nConverted:\n", df.dtypes, sep="")