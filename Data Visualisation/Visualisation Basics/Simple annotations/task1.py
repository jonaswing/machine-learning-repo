from matplotlib import pyplot as plt


fig, ax = plt.subplots()


x = [1, 2, 3, 4, 5]
y = [2, 4, 11, 4, 9]


ax.plot(x, y, color='red')
ax.set_title('MY PLOT')
ax.set_xlabel('X-Label')
ax.set_ylabel('Y-Label')

ax.text(2, 4, "2.0, 4.0")
ax.text(3, 11, 'Up here')
ax.text(4, 4, 'Down here')
ax.text(5, 9, '5.0, 9.0')

plt.show()


