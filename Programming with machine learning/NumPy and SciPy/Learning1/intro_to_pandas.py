import pandas as pd
import numpy as np

s = pd.Series(np.random.randint(10, size=5), index=["a","b","c","d","e"])

print(s)


d = {"a": 1, "b":2}
dictionary = pd.Series(d)

print(dictionary)


