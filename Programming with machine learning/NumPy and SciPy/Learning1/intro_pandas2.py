import pandas as pd
import numpy as np

d = {"a": 0.0, "b": 1.0, "c": 2.0}

dict_1 = pd.Series(d)

print(dict_1)


dict_2 = pd.Series(d, index=["b", "c", "d", "a"])


print(dict_2)



