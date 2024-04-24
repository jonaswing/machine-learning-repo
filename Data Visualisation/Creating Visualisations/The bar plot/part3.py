import matplotlib.pyplot as plt
import numpy as np

# Defines the data for the bar plot.
clinics = ["Clinic A", "Clinic B", "Clinic C", "Clinic D"]
first_time = np.array([5, 3, 4, 2])
routine = np.array([10, 20, 8, 12])
emergency = np.array([2, 4, 3, 5])

fig, ax = plt.subplots()
# Creates a bar plot for first-time clinic visits.
ax.bar(clinics, first_time, color="blue", label="First-time")
# Creates a bar plot for the routine clinic visits. Draws the bars' bottoms
# at the top of the first_time bars.
ax.bar(clinics, routine, bottom=first_time, color="purple", label="Routine")
# Creates a bar plot for the emergency clinic visits. Draws the bars' bottoms
# at the top of the height of both the first_time and routine bars added together.
ax.bar(clinics, emergency, bottom=np.add(first_time, routine), color="red", label="Emergency")
# Add detail to the Axes.
ax.set_title("Clinic visits per month ")
ax.set_xlabel("Clinics")
ax.set_ylabel("Number of visits")
# Add a Figure legend.
ax.legend()
# Display the Figure.
plt.show()