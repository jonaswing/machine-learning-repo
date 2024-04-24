from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Assuming 'data' is your DataFrame
data = pd.DataFrame({
    'feature_a': [29.53, 5.45, 1.71, 83.69, 3.48, 75.98, 65.43, 56.61, 84.43, 28.57, 37.97, 91.14, 10.12, 81.29, 75.97, 43.31, 46.17],
    'feature_b': [0.04, 0.778, 0.777, 0.928, 0.171, 0.188, 0.615, 0.902, 0.795, 0.959, 0.057, 0.945, 0.48, 0.219, 0.279, 0.827, 0.214],
    'feature_c': [22238, 16735, 14541, 17721, 12272, 14147, 24267, 19871, 10988, 19528, 15704, 17755, 16593, 8555, 8740, 13934, 3814],
    'feature_d': [7, 3, 10, 0, 1, 2, 6, 9, 8, 10, 1, 7, 9, 8, 7, 6, 7],
    'feature_e': ['South', 'South', 'South', 'South', 'South', 'West', 'South', 'South', 'West', 'East', 'South', 'East', 'North', 'North', 'West', 'West', 'South'],
    'class': ['Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High', 'Low', 'Low', 'Medium', 'Low']
})

# Initialize the OneHotEncoder
onehot = OneHotEncoder(dtype=int, sparse_output=True)

# Extract the 'feature_e' column and apply one-hot encoding
feature_e_numerical = pd.DataFrame(
    onehot.fit_transform(data[['feature_e']]).toarray(),
    columns=onehot.get_feature_names_out(['feature_e']))

# Drop the original 'feature_e' column from the DataFrame
data_encoded = data.drop(['feature_e'], axis=1)

# Concatenate the one-hot encoded features to the original DataFrame
data_encoded = pd.concat([data_encoded, feature_e_numerical], axis=1)

pd.set_option("display.max_columns", None)
# Display the resulting DataFrame
print(data_encoded)
