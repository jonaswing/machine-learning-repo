from sklearn import datasets
import pandas as pd

directories = pd.DataFrame(dir(datasets))


diabetes_data = pd.DataFrame(datasets.load_diabetes().data)

print(diabetes_data.head(20), "\n")


print(diabetes_data.DESCR)