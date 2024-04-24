import pandas as pd

data = {
    "Name": ["Tony","Robin", "Ane"],
    "Surname": ["Rony", "Tobin", "Ruud"],
    "Phone": [12345678, 87654321, 13243546]
}

pandas_data = pd.DataFrame(data)

print(pandas_data)