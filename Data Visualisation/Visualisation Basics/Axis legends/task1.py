from matplotlib import pyplot as plt


fig, ax = plt.subplots()


x1 = [1, 2, 2.5, 4, 10]
y1 = [2, 3, 3, 4.5, 6]

x2 = [1, 5, 6, 7, 10]
y2 = [2, 2, 1, 3, 4]

x3 = [1, 2, 2.5, 9, 10]
y3 = [2, 2.1, 2.2, 2, 2]

x4 = [1, 2, 2.5, 8, 10]
y4 = [2, 1, 2.5, 6, 5]

ax.plot(x1, y1, c='red', label='1')
ax.plot(x2, y2, c='blue', label='2')
ax.plot(x3, y3, c='green', label='3')
ax.plot(x4, y4, c='orange', label='4')

ax.grid(True)

ax.set_title('The Money Plot')

ax.legend(title='Legend', facecolor='beige', edgecolor='purple', shadow=True)

ax.annotate(text='Buy up', xy=(2, 1), xytext=(2.5, 1.5), arrowprops={'arrowstyle': 'simple'})
ax.annotate(text='Sell out, cash in, bro down',
            xy=(8, 6),
            xytext=(6, 5),
            arrowprops={'arrowstyle': 'simple'},
            c='lime',
            backgroundcolor='gold')


plt.show()

