import numpy as np
import pandas as pd

iris_data = pd.read_csv("IRIS.csv")

print(np.where(iris_data['sepal_length'] > 5.2))

