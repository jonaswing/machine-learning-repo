import matplotlib.pyplot as plt
import numpy as np


# Generate random sales values for 3 years.
year_1 = np.random.randint(1, 27000, 100)
year_2 = np.random.randint(1, 28000, 150)
year_3 = np.random.randint(1, 29000, 210)
# Define histogram arguments.
# Define the bin ranges.
bins = [1, 5000, 10000, 15000, 20000, 25000, 30000]
# Define the month names to be used as x-axis tick labels
bin_names = ["1 - 4999", "5000 - 9999", "10000 - 14999", "15000 - 19999", "20000-24999", "25000 - 30000"]
# Define the year names for the legend.
legend = ["Year one", "Year two", "Year three"]

fig, ax = plt.subplots()
# Create a histogram which divides the data into bins according to the predefined ranges.
ax.hist([year_1, year_2, year_3], bins=bins, label=legend)
# Add the horizontal grid lines.
ax.grid(axis="y")
# Add a legend.
ax.legend()
# Display the Figure.
plt.show()