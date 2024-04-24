import matplotlib.pyplot as plt
import numpy as np

# Generate x-axis coordinates
x_values = np.random.randint(0, 1000, 100)
x_values.sort()

# Generate y-axis coordinates
y_values = np.random.randint(0, 500, 100)

# Create the line plot
plt.plot(x_values, y_values, linestyle='--', marker='s', color='purple', label='Purple line')

# Set title
plt.title('A demo line plot')

# Add legend
plt.legend()

# Display the plot
plt.show()
