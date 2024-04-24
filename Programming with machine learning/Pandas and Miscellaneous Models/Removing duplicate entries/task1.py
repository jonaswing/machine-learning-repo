import pandas as pd

# Read the csv file
data = pd.read_csv('heart.csv')

# Turn the dataset into a pandas DataFrame
data = pd.DataFrame(data)

# Display the shape of the DataFrame
print("Shape: ",data.shape)

# Display 10 first rows and 20 last rows
print("First 10 rows: \n", data.head(11), "\nLast 20 rows: \n", data.tail(21))

# Display statistics about the dataset
print(data.describe())

# Display memory usage
print(data.memory_usage(index=False, deep=True))

# Change data type for Age
data['Age'] = data['Age'].astype('float64')
print(data)

# Data stats before removing duplicates
print(data.describe())
# Removing duplicates
data = data.drop_duplicates(keep='first')
# Data stats after removing duplicates
print(data.describe())

# Save the updated data to a new csv file
data.to_csv('updated_heart.csv')

# Data stats of the updated data
description_of_data = data.describe()

# Save csv file with the updated data stats
description_of_data.to_csv('heart_statistics.csv')

