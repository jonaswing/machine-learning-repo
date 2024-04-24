import matplotlib.pyplot as plt
import numpy as np


x1 = [1,9]
y1 = [1,9]
z1 = [1,9]

x2 = [1,8]
y2 = [2,8]
z2 = [1,9]

x3 = [1,7]
y3 = [3,7]
z3 = [1,9]

fig = plt.figure()


ax = plt.axes(projection='3d')

ax.plot3D(x1, y1, z1, 'blue', label='The blue line')
ax.plot3D(x2, y2, z2, 'red', label='The red line')
ax.plot3D(x3, y3, z3, 'green', label='The green line')

ax.legend()

plt.show()


