from matplotlib import pyplot as plt
import pandas as pd

# Request a Figure (fig) and 2 Axes (ax) objects
# using subplots().
fig, ax = plt.subplots(2, )

# Define the data for the plots.
x = [[1,1], [2,2], [3, 3], [4, 4], [5, 5]]
y = [[1,2], [2,4], [3, 6], [4, 8], [5, 10]]
data = pd.DataFrame({"col1": [1, 2, 3, 4, 5],
                     "col2": [1, 2, 3, 4, 5],
                     "col3": [2, 4, 6, 8, 10]})

# Plot the data on the first Axis, including a title and the legend.
# The data is plotted using multi-dimensional lists.
ax[0].plot(x, y, label=["First line", "Second line"])
ax[0].set_title("Using multi-dimensional data")
ax[0].legend()
# Plot the data on the second Axis, including a title and the legend.
# The data is plotted using a Pandas DataFrame.
ax[1].plot("col1", "col2", label="First line", data=data)
ax[1].plot("col1", "col3", label="Second line", data=data)
ax[1].set_title("Using a DataFrame")
ax[1].legend()
# Change the layout to tight, to make use of the entire Figure.
plt.tight_layout()
# Display the Figure.
plt.show()