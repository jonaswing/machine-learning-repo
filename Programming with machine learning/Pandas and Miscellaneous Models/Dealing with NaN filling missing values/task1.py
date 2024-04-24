import pandas as pd
import numpy as np

data = pd.read_csv('IRIS.csv')
data = pd.DataFrame(data)


# The original dataset
print("Original dataset: \n", data.shape, "\n", data.head(10), "\n")


# Remove all missing value rows in dataset
remove_nan = data.dropna()
print("Remove all Nan's: \n", remove_nan.shape, "\n", remove_nan.head(10), "\n")


# Remove missing value rows in 'species' column
data = data.dropna(subset=['species'])
print("Remove all Nan's in species: \n", data.shape, "\n", data.head(10), "\n")


# Removes the entire species column
remove_species = data.drop(['species'], axis=1)
print("Remove entire species column: \n", remove_species.head(10), "\n")


# Replace NaN values in sepal_length, sepal_width, petal_length, and petal_width columns with median
columns_to_fill = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
for column in columns_to_fill:
    median_value = data[column].median()
    data[column].fillna(median_value, inplace=True)
print("Replace Nan's with median: \n", data.shape, "\n", data.head(10))