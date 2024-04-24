from matplotlib import pyplot as plt


fig, ax = plt.subplots()
x = [1, 2, 3, 4, 5]
y = [2, 4, 11, 4, 9]
ax.plot(x, y, color="green", linewidth=5, linestyle="dashed")
# Change the scale to log.
ax.set_xscale("log")
ax.set_yscale("log")
plt.show()


