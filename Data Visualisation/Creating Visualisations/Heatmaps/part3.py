import numpy as np
import matplotlib.pyplot as plt

courses = ["PL", "PR", "DM", "DP", "ML", "CI", "DV"]
students = ["Arud, Karoline", "Ege, Jens", "Grinde, Karl", "Odden, Eli", "Manger, Arvid", "Skagen, Laila", "Waag, Silje"]

student_results = np.array([[39, 48, 50, 79, 54, 64, 97],
                            [61, 43, 34, 99, 23, 69, 54],
                            [44, 38, 90, 35, 78, 67, 54],
                            [30, 71, 27, 33, 21, 24, 60],
                            [42, 27, 92, 56, 52, 98, 76],
                            [67, 34, 28, 55, 59, 55, 65],
                            [69, 82, 55, 73, 78, 23, 61]])

fig, ax = plt.subplots()
# Use the Axes object's imshow function to create a heatmap.
# The heatmap is created using the RdYlGn (RedYellowGreen) colormap.
im = ax.imshow(student_results, cmap="RdYlGn")
# Show all ticks and label them with the entries from the lists.
# For each axis, the number of ticks is equivalent to the number
# of elements in the list.
ax.set_xticks(np.arange(len(students)), labels=students)
ax.set_yticks(np.arange(len(courses)), labels=courses)
# Rotate the tick labels and modify their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
# Set the title of the Axes object.
ax.set_title("Student results on the AML Programme")
# Make the most use of the Figure area.
fig.tight_layout()


# Add a colorbar to the plot.
fig.colorbar(im)
# Iterage over the data dimensions and create text annotations.
for i in range(len(courses)):
    for j in range(len(students)):
        # For each data point, add an annotation consisting of the value.
        # The value is displayed horizontally and vertically centered.
        # Values that are low or high are displayed in white and others in black.
        # Changing text colours is not always necessary, but may improve
        # legibility if the text colour is lost against the background colour
        # of the plot.

        if student_results[i, j] < 25 or student_results[i,j] > 75:
            color = "white"
        else:
            color = "black"

        ax.text(j, i, student_results[i, j], ha="center", va="center", color=color)
# Display the plot.
plt.show()