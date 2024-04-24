import pandas as pd
import numpy as np
from sklearn.preprocessing import FunctionTransformer

data = np.random.randint(500, size=(500, 1))
demo = pd.DataFrame(data, columns=['Feature 1'])
print(data)


def MyBinarizer(X, threshold=0.0):
    # Change all values above the threshold to 1 and the rest to 0
    # returns the modified Numpy array
    return np.where(X % 3.5 == 0, 1, 0)


binary = FunctionTransformer(func=MyBinarizer)
demo["Feature 1_binary"] = binary.transform(demo["Feature 1"].values.reshape(-1,1))

print(demo.head(20))



