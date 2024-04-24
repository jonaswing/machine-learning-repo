from matplotlib import pyplot as plt


fig, ax = plt.subplots()

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 11, 4, 9]

x2 = [1, 2, 3, 4, 5]
y2 = [7, 15, 20, 25, 30]


ax.plot(x1, y1, color='orange', linewidth=2, linestyle='dashed')
ax.plot(x2, y2, c='blue', lw=9, ls='dashed')

plt.show()

