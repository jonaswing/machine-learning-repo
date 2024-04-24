import pandas as pd
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer


# Create DataFrame with 2 columns with 50 values each
data = np.random.randint(50, size=(50, 2))
demo = pd.DataFrame(data, columns=['Feature_1', 'Feature_2'])
print(demo.head(10), "\n")


# Binning feature_1
bin_feature_1 = KBinsDiscretizer(n_bins=7, strategy='uniform', encode='ordinal')
demo["Feature_1_uniform_2"] = bin_feature_1.fit_transform(demo["Feature_1"].values.reshape(-1,1))

print("Binning feature_1: \n", demo.head(10), "\n")


# Binning feature_2
bin_feature_2 = KBinsDiscretizer(n_bins=3, strategy='uniform', encode='ordinal')
demo["Feature_2_uniform_2"] = bin_feature_2.fit_transform(demo["Feature_2"].values.reshape(-1,1))

print("Binning feature_2: \n", demo.head(10), "\n")



