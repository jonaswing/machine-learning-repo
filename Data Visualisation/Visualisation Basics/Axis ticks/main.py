# Import pyplot from matplotlib as plt.
from matplotlib import pyplot as plt
# Import various Formatters and Locators
from matplotlib.ticker import NullFormatter, \
    AutoMinorLocator, MaxNLocator

fig, ax = plt.subplots()
x = [1, 2, 3, 4, 5]
y = [2, 4, 11, 4, 9]
ax.plot(x, y, color="green", linewidth=5, linestyle="dashed")
# Modify the details of the ticks.
# Hide the major tick labels for the x-axis
ax.xaxis.set_major_formatter(NullFormatter())
# Include minor tick marks on the x-axis, with scalar values.
ax.xaxis.set_minor_locator(AutoMinorLocator())
# Change the y-axis locator to a predefined number of values (2).
ax.yaxis.set_major_locator(MaxNLocator(2))
plt.show()
