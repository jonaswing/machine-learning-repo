import numpy as np
import pandas as pd


# Import dataset
data = pd.read_csv('water_potability.csv')
data = pd.DataFrame(data)


# Check how many missing values
print(data.isnull().sum())


# Check skewness
skewness = data.skew()
print(skewness)


# Fill missing Sulfate
data['Sulfate'].fillna(data['Sulfate'].mean(), inplace=True)
# Fill missing ph
data['ph'].fillna(data['ph'].mean(), inplace=True)
# Fill missing Trihalomethanes
data['Trihalomethanes'].fillna(data['Trihalomethanes'].mean(), inplace=True)


# Save updated csv file
# Save the modified DataFrame as a new CSV file
data.to_csv('updated_water_potability.csv', index=False)


# Check how many missing values
print(data.isnull().sum())


# Choosing target to predict
X = data.drop('Potability', axis=1)
y = data['Potability']






