import numpy as np
import pandas as pd

data = np.genfromtxt('marketing_campaign.csv', delimiter=',', dtype=object)

array_1 = data[0:1]

array_2 = data[1:16]

min_value = np.min(array_2)
max_value = np.max(array_2)

normalised_array_2 = array_2

print(array_1)
print()
print(array_2)


