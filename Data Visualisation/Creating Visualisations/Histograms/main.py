import matplotlib.pyplot as plt
import numpy as np

# Generate 100 random values in the range 0 to 500.
data = np.random.randint(0, 500, 100)

fig, ax = plt.subplots()
# Create a histogram which divides the data into 10 bins.
ax.hist(data, bins=10, linewidth=1, color="lightgray", edgecolor="blue")
# Display the Figure.
plt.show()
fig.savefig("Histogram.jpg")