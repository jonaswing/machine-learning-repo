import matplotlib.pyplot as plt
import numpy as np

# Generate z, x and y coordinates.
# The linspace method is used to generate a sequence
# of 100 evenly spaced values between 0 and 50
z = np.linspace(0, 50, 100)
# For each of the values in z an associated x value is
# calculated by calculating the sine of the value.
# Random values could have been generated, but the line may
# have looked like a scribble.
x = np.sin(z)
# For each of the values in z an associated y value is
# calculated by calculating the cosine of the value.
# Random values could have been generated, but the line may
# have looked like a scribble.
y = np.cos(z)

# Create a Figure.
fig = plt.figure()
# Create a new Axes object associated with the current figure.
# Setting the projection to 3d, creates a 3D plot.
ax = plt.axes(projection ='3d')
# Plot a blue 3D line and associate a label with it.
ax.plot3D(x, y, z, "blue", label="The line")
# Add a legend to the Axes.
ax.legend()
# Display the plot.
plt.show()