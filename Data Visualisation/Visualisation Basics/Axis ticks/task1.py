from matplotlib import pyplot as plt
from matplotlib.ticker import AutoLocator, PercentFormatter, FixedFormatter, FixedLocator

fig, ax = plt.subplots()
x = [1, 2, 3, 4, 5]
y = [2, 4, 11, 4, 9]
ax.plot(x, y, color="green", linewidth=5, linestyle="dashed")


x_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
ax.xaxis.set_major_locator(FixedLocator(range(1, len(x) + 1)))
ax.xaxis.set_major_formatter(FixedFormatter(seq=x_labels))
ax.yaxis.set_major_formatter(PercentFormatter())


plt.show()

