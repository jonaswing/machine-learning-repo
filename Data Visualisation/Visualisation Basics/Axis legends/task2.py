import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Data
x = np.arange(0, 101)
y2 = np.random.randint(1, 301, size=len(x))
y3 = np.random.randint(1, 201, size=len(x))
y4 = np.random.randint(1, 151, size=len(x))


fig, ax = plt.subplots()

# Plot
ax.plot(x, y2, c='red', label='Oriental carpet from Iran')
ax.plot(x, y3, c='green', label='Carpet from Sweden')
ax.plot(x, y4, c='blue', label='Carpet from Moss')

# Text
ax.set_title('Price over time')
plt.xlabel('Time')
plt.ylabel('Price')

# Annotation
plt.annotate(text='Red is high', xy=(50, 201), xytext=(50, 220), arrowprops={'arrowstyle':'simple'})
plt.annotate(text='', xy=(20, 201), xytext=(20, 240), arrowprops=dict(facecolor='purple'))
ax.text(0, 260, r'$\sqrt{(\frac{a^2 + b^2}{c^2})^2}$')

# Legend
plt.legend(title='THIS IS A LEGEND', ncol=2, facecolor='beige', edgecolor='orange', fontsize='large')


plt.show()



