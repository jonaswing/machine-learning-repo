import matplotlib.pyplot as plt
import numpy as np

# Generate data
set_1 = np.random.randint(40, 100, 50)
set_2 = np.random.randint(10, 200, 80)
set_3 = np.random.randint(120, 180, 90)
set_4 = np.random.randint(80, 160, 60)

fig, ax = plt.subplots()
# Create a horizontal box plot for the 4 data sets.
# The whiskers are set at the 10th and 90th percentile.
# Fliers are drawn as green circles.
ax.boxplot([set_1, set_2, set_3, set_4],
           labels=["Set 1", "Set 2", "Set 3", "Set 4"],
           vert=False,
           whis=(10,90),
           sym="go")
# Display the Figure.
plt.show()
