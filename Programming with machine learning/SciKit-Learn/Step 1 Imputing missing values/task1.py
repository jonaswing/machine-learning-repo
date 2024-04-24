import pandas as pd
import numpy as np
from sklearn.impute import MissingIndicator
from sklearn.impute import SimpleImputer


data = pd.read_csv('data0301.csv')
data = pd.DataFrame(data)

print(data.shape)

# Drop rows with more than two missing values (there are 6 columns all together, 6 - 2 = 4)
data = data.dropna(thresh=4)
print(data.shape)
print(data.head(20))

# Reset index after removing missing value rows
data.reset_index(inplace=True)
data.drop(['index'], axis=1, inplace=True)
print(data.shape)


# Fill nans with -1
data = data.fillna(-1)
print(data.head(20), "\n")


# Replace feature_a missing values with the features mean
data['feature_a'].replace({-1:data['feature_a'].mean()}, inplace=True)
print("Replace feature_a with mean:\n", data.head(20), "\n")


# Replace feature_b missing values with the features median
data['feature_b'].replace({-1:data['feature_a'].median()}, inplace=True)
print("Replace feature_b with median:\n", data.head(40), "\n")


# Replace feature_c with 10000
data['feature_c'].replace({-1: 10000}, inplace=True)
print("Replace feature_c with 10000:\n", data.head(20), "\n")


# Replace feature_d with 3
data['feature_d'].replace({-1: 3}, inplace=True)
print("Replace feature_d with 3:\n", data.head(20), "\n")



# Create a SimpleImputer to replace NaN with the most frequent value
imputer = SimpleImputer(missing_values=-1, strategy="most_frequent")
# Replace feature_e with most frequent value
# Fit and transform the imputer on 'feature_e' column
data['feature_e'] = imputer.fit_transform(data[['feature_e']])
print("Replace feature_e with most frequent:\n", data.head(20), "\n")


# Replace feature_e with most frequent value
data['class'] = imputer.fit_transform(data[['class']])
print("Replace class with most frequent:\n", data.head(20), "\n")


data.to_csv('data0301_imputed.csv')



