import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer

# Step 1: Import the data set into a Pandas DataFrame
url = "data0302.csv"  # Replace with the actual path to your downloaded file
df = pd.read_csv(url)

# Step 2: Display the current shape of the DataFrame
print("Current Shape of the DataFrame:", df.shape)

# Step 3: Display the first 20 rows of the DataFrame
print("First 20 rows of the DataFrame:")
print(df.head(20))

# Step 4: Define custom transformations
def custom_transformation(column):
    return column * 7.2

# Step 5: Create a pipeline for transformations
preprocessor = ColumnTransformer(
    transformers=[
        ('feature_a', KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform'), ['feature_a']),
        ('feature_c', FunctionTransformer(lambda x: x > 17500, validate=False), ['feature_c']),
        ('feature_d', FunctionTransformer(custom_transformation, validate=False), ['feature_d']),
        ('feature_e', OneHotEncoder(drop='first'), ['feature_e']),
        ('class', FunctionTransformer(lambda x: pd.Categorical(x).codes, validate=False), ['class']),
    ])

# Step 6: Apply transformations
processed_data = preprocessor.fit_transform(df)

# Step 7: Create a new DataFrame with the transformed data
columns = ['feature_a', 'feature_b', 'feature_c', 'feature_d', 'feature_e_1', 'feature_e_2', 'feature_e_3', 'feature_e_4', 'class']
processed_df = pd.DataFrame(processed_data, columns=columns)

# Step 8: Save the revised data set as data0302_modified.csv
processed_df.to_csv("data0302_modified_gipiti.csv", index=False)
