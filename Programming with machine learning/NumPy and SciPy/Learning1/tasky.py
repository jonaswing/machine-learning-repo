
import numpy as np


data = np.random.randint(227, size=(5, 10))


data_copy = data.copy()


data_copy = np.sort(data_copy)


print("\nCopied and sorted:\n", data_copy)