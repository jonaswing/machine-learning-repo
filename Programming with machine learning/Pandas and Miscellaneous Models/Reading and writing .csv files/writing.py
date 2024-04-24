# Import pandas with the alias pd
import pandas as pd

data = {
    "Name": ["Tony","Robin", "Ane"],
    "Surname": ["Rony", "Tobin", "Ruud"],
    "Phone": [12345678, 87654321, 13243546]
}

data = pd.Series(data)

# Writes the content of the data frame to file
data.to_csv("written_csv/output.csv")
# Writes the content of the data frame as a tab-separated file
data.to_csv("written_csv/tab_output.csv", sep="\t")
# Writes the content of the data frame without the index or header
data.to_csv("written_csv/no_header_or_index_output.csv", header=False, index=False)

