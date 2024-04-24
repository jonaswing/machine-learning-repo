import numpy as np

data = np.random.rand(500, 5)

print("The values from the 100th to the 200th row, including only the last three columns: \n",
      data[100:201,-3:])