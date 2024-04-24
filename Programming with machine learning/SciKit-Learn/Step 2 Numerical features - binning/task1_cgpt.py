import numpy as np
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

# Generate a data set containing 50 random values for each column
data = {
    "Column_1": np.random.rand(50),
    "Column_2": np.random.rand(50)
}

dataset = pd.DataFrame(data)

# Create a KBinsDiscretizer for Column_1 with 7 bins using the quantile strategy and ordinal encoding
disc_column_1 = KBinsDiscretizer(n_bins=7, strategy="quantile", encode="ordinal")
# Add the encoded attribute as a new feature to the dataset
dataset["Column_1_binned"] = disc_column_1.fit_transform(dataset["Column_1"].values.reshape(-1, 1))

# Create a KBinsDiscretizer for Column_2 with 3 bins using the uniform strategy and ordinal encoding
disc_column_2 = KBinsDiscretizer(n_bins=3, strategy="uniform", encode="ordinal")
# Add the encoded attribute as a new feature to the dataset
dataset["Column_2_binned"] = disc_column_2.fit_transform(dataset["Column_2"].values.reshape(-1, 1))

# Display the first 10 rows of the dataset
print(dataset.head(10))
