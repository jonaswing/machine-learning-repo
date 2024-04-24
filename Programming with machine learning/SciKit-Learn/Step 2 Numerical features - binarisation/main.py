# import numpy under the alias np and
# pandas under the alias pd
import numpy as np
import pandas as pd
# import Binarizer from the scikit-learn.preprocessing module
from sklearn.preprocessing import Binarizer

# Generate a data set containing 250 random integers in the range 0 to 1000
# in a single column.
data = np.random.randint(1000, size=(250,1))
demo = pd.DataFrame(data, columns=["Feature 1"])

# Create a Binarizer with a threshold of 350.  It's set to return a new array (copy=True).
binary = Binarizer(threshold=350, copy=True)
demo["Feature 1_binary"] = binary.fit_transform(demo["Feature 1"].values.reshape(-1,1))
# Display the first 10 rows of the data set
print(demo.head(10))