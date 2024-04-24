import pandas as pd

# Read the IRIS.csv file
iris_data = pd.read_csv('IRIS.csv')

# Return only the first 100 rows
iris_data = iris_data.head(10)

# Return only the columns related to the petal, along with the label
petal_columns = ['petal_length', 'petal_width', 'species']
iris_data = iris_data[petal_columns]

# Ensure numeric values are returned as integers
iris_data[['petal_length', 'petal_width']] = iris_data[['petal_length', 'petal_width']].apply(pd.to_numeric, errors='coerce').fillna(99).astype(int)

# Set all missing string values to 'Missing'
iris_data['species'] = iris_data['species'].fillna('Missing')

# Display the resulting dataframe
print(iris_data)

