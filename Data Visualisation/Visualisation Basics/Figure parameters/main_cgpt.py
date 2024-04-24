import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Modify figure attributes directly
fig.set_size_inches(19.20, 10.80)  # Set the figure size to 19.20 by 10.80 inches
fig.patch.set_facecolor('white')   # Set the background color to white
fig.patch.set_edgecolor('white')   # Set the edge color to white
fig.patch.set_linewidth(0)         # Remove the figure's frame

# Modify font attributes through rcparams
plt.rcParams.update({"font.size": 22, "font.weight": "bold"})

# Plot something (optional)
ax.plot([1, 2, 3], [4, 5, 6])

# Show the plot
plt.show()
