import numpy as np
import matplotlib.pyplot as plt

# Generate data
np.random.seed(0)  # for reproducibility
x = np.sort(np.random.randint(120, 271, 78))
y1 = np.random.randint(40, 181, 78)
y2 = np.random.randint(50, 351, 78)
y3 = np.random.randint(70, 291, 78)
y4 = np.random.randint(55, 101, 78)

# Create Figure and Axes
fig, axs = plt.subplots(2, 2, figsize=(19.20, 10.80))

# Plot data
axs[0, 0].plot(x, y1)
axs[0, 0].grid(True)
axs[0, 0].tick_params(which='both', direction='in', width=2)
axs[0, 0].minorticks_on()

axs[0, 1].plot(x, y2)
axs[0, 1].yaxis.set_ticklabels([])
axs[0, 1].tick_params(axis='y', width=0)
axs[0, 1].tick_params(axis='x', which='both', direction='in', width=2)
axs[0, 1].minorticks_on()

axs[1, 0].plot(x, y3)
axs[1, 0].tick_params(which='both', direction='in', width=2)
axs[1, 0].minorticks_on()

axs[1, 1].plot(x, y4)
axs[1, 1].tick_params(which='both', direction='in', width=2)
axs[1, 1].minorticks_on()

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('subplot_figure.jpg', dpi=300)
plt.show()
