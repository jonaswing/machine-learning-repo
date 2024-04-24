import pandas as pd
import numpy as np

iris_data = pd.read_csv('IRIS.csv')

# Select the first 50 rows and specific columns
modified_data = iris_data.iloc[:50, [2, 3, 4]]

# Rename the columns
modified_data.columns = ['petal_length', 'petal_width', 'species']

# Save the modified dataset to a new CSV file
modified_data.to_csv('Iris_modified.csv', index=False)


print(modified_data)

