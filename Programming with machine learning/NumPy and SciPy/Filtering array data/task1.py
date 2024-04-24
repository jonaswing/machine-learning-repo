import numpy as np

data = np.random.randint(100, size=(10, 2))

filter1 = data < 50

filter2 = data % 5 == 0

print(data, "\n")

print(data[filter1], "\n")

print(data[filter2])

