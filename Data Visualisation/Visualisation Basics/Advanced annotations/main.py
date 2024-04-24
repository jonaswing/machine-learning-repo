# Import pyplot from matplotlib as plt.
from matplotlib import pyplot as plt

# Request a Figure (fig) and Axes (ax) object
# using subplots().
fig, ax = plt.subplots()
# Define the x and y coordinates.
x = [1, 2, 3, 4, 5]
y = [2, 4, 11, 4, 9]
# Draw a line using the x and y coordinates.
# ax.plot(x, y)
# Draw a styled line using the x and y coordinates.
ax.plot(x, y, color="green", linewidth=5, linestyle="dashed")
ax.set_title("A simple plot")
ax.set_xlabel("The details for the x-axis")
ax.set_ylabel("The details for the y-axis")


# Previous statements to plot the figure and labels

ax.annotate("Simple (simple)", xy=(2, 4), xytext=(1.3, 2),
            arrowprops={"width": 10, "headwidth": 15, "headlength": 15})
ax.annotate("Simple (fancy and curved)", xy=(4, 4), xytext=(3, 2),
            arrowprops={"arrowstyle": "simple", "connectionstyle": "angle3"})
ax.annotate("Fancy", xy=(3, 11), xytext=(1.3, 10.5),
            arrowprops=dict(arrowstyle="fancy", color= "purple"))
ax.annotate("Wedge", xy=(5, 9), xytext=(4, 10.5),
            arrowprops=dict(arrowstyle="wedge",
                            facecolor="white",
                            edgecolor="orange"))

# Display the plotted figure.
plt.show()

