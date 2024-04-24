import pandas as pd


data_1 = {
    "customer_id": [1,2,3,4,5],
    "name": ["Jonas", "Tony", "Rony", "Dan", "Mike"],
    "surname": ["Wingan", "Dony", "Mony", "Zan", "Spike"]
}

data_2 = {
    "customer_id": [4,5,8,9,10],
    "transaction_id": [234,456,678,789,890],
    "value": [999,888,777,666,555]
}

data_1 = pd.DataFrame(data_1)
data_2 = pd.DataFrame(data_2)

print(data_1, "\n")
print(data_2, "\n")

print("Inner: \n", data_1.merge(data_2, on='customer_id', how='inner'), "\n")

print("Outer: \n", data_1.merge(data_2, on='customer_id', how='outer'), "\n")

print("Left: \n", data_1.merge(data_2, on='customer_id', how='left'), "\n")

print("Right: \n", data_1.merge(data_2, on='customer_id', how='right'), "\n")