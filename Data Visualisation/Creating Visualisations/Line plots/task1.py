import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# Generate 100 random values in the range 0 to 1000
x1 = np.random.randint(0, 1001, 100)
# Sort the values from low to high
x1 = np.sort(x1)

# Generate 100 random values in the range 0 to 500
y1 = np.random.randint(0, 501, 100)


# Create the two line plots and show the figure.
plt.plot(x1, y1, c='purple', ls='dashed', marker='s')
plt.xlabel('x')
plt.ylabel('y')
plt.title('A demo line plot')
plt.legend(['Purple line'])
plt.show()




