import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
import sklearn.preprocessing as pre


# Read csv
data = pd.read_csv('data0303.csv')
data = pd.DataFrame(data)


# Print data
print("Data shape: \n", data.shape, "\n")
print("First 20 rows: \n", data.head(20), "\n")


# Split 80/20 training/test
train, test = train_test_split(data, test_size=.2, random_state=1)

print("Train set: \n", train)
print()
print("Test set:\n", test)


# STANDARD SCALER
# Declare a StandardScaler
scaler = StandardScaler()
# Use the scaler to scale the values of each column
train["feature_a"] = scaler.fit_transform(train["feature_a"].values.reshape(-1, 1))
train["feature_b"] = scaler.fit_transform(train["feature_b"].values.reshape(-1, 1))
train["feature_d"] = scaler.fit_transform(train["feature_d"].values.reshape(-1, 1))

print("StandardScaler: \n", train.head(20))


# MIN MAX SCALER
scaler = MinMaxScaler()
# Use the scaler to scale the values of each column
train["feature_a"] = scaler.fit_transform(train["feature_a"].values.reshape(-1, 1))
train["feature_b"] = scaler.fit_transform(train["feature_b"].values.reshape(-1, 1))
train["feature_d"] = scaler.fit_transform(train["feature_d"].values.reshape(-1, 1))

print("MinMaxScaler: \n", train.head(20))


# MAX ABS SCALER
scaler = MaxAbsScaler()
# Use the scaler to scale the values of each column
train["feature_a"] = scaler.fit_transform(train["feature_a"].values.reshape(-1, 1))
train["feature_b"] = scaler.fit_transform(train["feature_b"].values.reshape(-1, 1))
train["feature_d"] = scaler.fit_transform(train["feature_d"].values.reshape(-1, 1))

print("MaxAbsScaler: \n", train.head(20))


## MAX NORMALISATION
## Performs max normalisation and stores the result
#train_max_normalized = pre.normalize(train[['feature_a', 'feature_b', 'feature_d']], norm="max", axis=0)
## Converts the result to a DataFrame
# = pd.DataFrame(train_max_normalized, columns=['feature_a', 'feature_b', 'feature_d'])
## Output the results of performing l1 normalisation
#print("\nData set after max normalisation:\n", train_max_normalized)

#train_max_normalized = train.merge(train, how='outer')

#print("Max normalisation: \n", train_max_normalized)


# L1 NORMALISATION
# Performs l1 normalisation and stores the result
l1_results = pre.normalize(train[['feature_a', 'feature_b', 'feature_d']], norm="l1")
# Converts the result to a DataFrame
l1_results = pd.DataFrame(l1_results, columns=['feature_a', 'feature_b', 'feature_d'])



# Output the results of performing l1 normalisation
print("\nData set after l1 normalisation:\n", l1_results)

