import pandas as pd
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv('data0302.csv')
data = pd.DataFrame(data)

print(data.shape)
print(data.head(20), "\n")


bin_feature_a = KBinsDiscretizer(n_bins=10, strategy='uniform', encode='ordinal')
data['feature_a'] = bin_feature_a.fit_transform(data['feature_a'].values.reshape(-1,1))

print(data.head(10), "\n")


def MyBinarizer(X, threshold=17500):
    return np.where(X > threshold, 1, 0)

binary = FunctionTransformer(func=MyBinarizer,kw_args={"threshold":17500})
data["feature_c_binary"] = binary.transform(data["feature_c"].values.reshape(-1,1))


print(data.head(10), "\n")


data['feature_d_multiplied'] = [each * 7.2 for each in data['feature_d']]

# pd.set_option('display.max_columns', None)
print(data.head(10), "\n")


onehot = OneHotEncoder(dtype=int, sparse_output=True)

# Extract the 'feature_e' column and apply one-hot encoding
feature_e_numerical = pd.DataFrame(
    onehot.fit_transform(data[['feature_e']]).toarray(),
    columns=onehot.get_feature_names_out(['feature_e']))

# Drop the original 'feature_e' column from the DataFrame
data = data.drop(['feature_e'], axis=1)

# Concatenate the one-hot encoded features to the original DataFrame
data = pd.concat([data, feature_e_numerical], axis=1)

print(data.head(10))


# Create a LabelEncoder object
label_encoder = LabelEncoder()

# Fit and transform the 'class' column
data['class'] = label_encoder.fit_transform(data['class'])

class_mapping = {'Low': 0, 'Medium': 1, 'High': 2}

data['class'] = data['class'].map(class_mapping)

print(data.head(10))

data.to_csv('data0302_modified.csv')



