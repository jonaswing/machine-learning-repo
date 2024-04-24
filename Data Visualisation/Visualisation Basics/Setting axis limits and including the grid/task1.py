from matplotlib import pyplot as plt


fig, ax = plt.subplots()


x = [1,2,3,4,5]
y = [2,3,5,2,3]

ax.plot(x, y, c='red')
ax.axis([1,5,2,5])
ax.grid(True, ls='dashdot', lw=2, c='blue')

plt.show()


