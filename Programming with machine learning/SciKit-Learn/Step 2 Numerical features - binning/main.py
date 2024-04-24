# import numpy under the alias np and
# pandas under the alias pd
import numpy as np
import pandas as pd
# import KBinsDiscretizer from the scikit-learn.preprocessing module
from sklearn.preprocessing import KBinsDiscretizer

# Generate a data set containing 250 random integers in the range 0 to 1000
# in a single column.
data = np.random.randint(1000, size=(250,1))
demo = pd.DataFrame(data, columns=["Feature 1"])

# Create a KBinsDiscretizer to encode Feature 1 as 4 bins, using the quantile strategy
# and ordinal encoding
disc = KBinsDiscretizer(n_bins=4, strategy="uniform", encode="ordinal")
# Add the encoded attribute as a new feature to the data set.
demo["Feature 1_uniform_2"] = disc.fit_transform(demo["Feature 1"].values.reshape(-1,1))
# Display the first 10 rows of the data set
# The same approach, but now using 10 bins
disc = KBinsDiscretizer(n_bins=10, strategy="kmeans", encode="ordinal")
# Add the encoded attribute as a new feature to the data set.
demo["Feature 1_uniform_10"] = disc.fit_transform(demo["Feature 1"].values.reshape(-1,1))
# Display the first 10 rows of the data set
print(demo.head(10))