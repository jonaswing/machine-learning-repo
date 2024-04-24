from matplotlib import pyplot as plt
# Request a Figure (fig) and Axes (ax) object
# using subplots().
fig, ax = plt.subplots()
# Draw a styled line using the x and y coordinates.
ax.set_title(r"Rendered using TeX: $\sqrt{(\frac{a^2 + b^2}{c^2})^2}$")
ax.set_xlabel(r"$\{2,4,6,\ldots ,n\}$")
ax.set_ylabel(r"$\sum_{i=1}^{n}i=\frac{n(n+7)}{2}$")
ax.text(0.5, 0.5, "$\prod_{i=1}^ni=n!$")
# Display the plotted figure.
plt.show()