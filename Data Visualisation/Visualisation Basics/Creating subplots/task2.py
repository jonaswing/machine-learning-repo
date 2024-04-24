from matplotlib import pyplot as plt
import numpy as np
import random


# Data 1
x1 = [random.randint(120, 270) for _ in range(78)]
x1.sort(reverse=True)

# Data 2
y1 = [random.randint(40, 180) for _ in range(78)]

# Data 3
y2 = [random.randint(50, 350) for _ in range(78)]

# Data 4
y3 = [random.randint(70, 290) for _ in range(78)]

# Data 5
y4 = [random.randint(55, 100) for _ in range(78)]


# Create figure
fig, axs = plt.subplots(4, sharex=True, sharey="row")
# Remove the horizontally spanning space between the sub-plots.
fig.subplots_adjust(hspace=0)
# Plot a line on the first Axis.
axs[0].plot(x1, y1)
# Plot a line on the second Axis.
axs[1].plot(x1, y2)
# Plot a line on the third Axis.
axs[2].plot(x1, y3)
# Plot a line on the fourth Axis.
axs[3].plot(x1, y4)

plt.show()


