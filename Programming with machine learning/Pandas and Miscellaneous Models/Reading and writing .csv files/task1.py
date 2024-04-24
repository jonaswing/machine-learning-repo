import pandas as pd


data = {
    "Name": ["Roger", "Doger", "Tony", "Rony"],
    "Surname": ["Yaba", "Daba", "Corny", "Williams"],
    "Phone": [23454345, 23454567, 23457658, 21324354]
}

data = pd.Series(data)


data.to_csv("family_output.csv", header=False)