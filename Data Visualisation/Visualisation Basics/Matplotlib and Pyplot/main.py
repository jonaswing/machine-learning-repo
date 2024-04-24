# Import pyplot from matplotlib as plt.
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 3, 27, 23]

# The OOP-based approach. First generate Figure and
# Axes objects and call methods on them.
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Using OOP")
plt.show()

# The pyplot approach. Calling functions directly
# from pyplot.
# Clear the current Figure. Alternatively cla() clears
# the current Axes.
plt.clf()
plt.plot(x, y)
plt.title("Using pyplot")
plt.show()