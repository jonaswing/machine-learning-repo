import numpy as np

data = np.random.randint(0, 100, size=50).reshape(5,10)

divide_data = np.random.randint(0, 100, size=1)

new_data = data / divide_data
new_data = np.round(new_data, 2).reshape(5,10)

print("Original data: \n", data)
print()

print("Number to divide by: \n", divide_data)
print()

print("New data: \n", new_data)
