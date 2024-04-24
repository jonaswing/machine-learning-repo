import pandas as pd
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

# Read CSV file and replace NaN values in 'class' column with a default value
data = pd.read_csv('data0302.csv').fillna({'class': 'Unknown'})
data = pd.DataFrame(data)

print(data.shape)
print(data.head(20), "\n")

# ... (your existing code for transformations)

# Create a LabelEncoder object
label_encoder = LabelEncoder()

# Fit and transform the 'class' column
data['class'] = label_encoder.fit_transform(data['class'])

class_mapping = {'Low': 0, 'Medium': 1, 'High': 2}

data['class'] = data['class'].map(class_mapping)

print(data.head(10))

data.to_csv('data0302_modified2.csv', index=False)
