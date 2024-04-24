from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt


# Load the Iris dataset
iris = load_iris()


# Assign column names to the features
feature_names = iris.feature_names

# Convert feature data to a pandas DataFrame with column names
X = pd.DataFrame(data=iris.data, columns=feature_names)


selected = (X['sepal length (cm)'])

bins = [4, 5, 6, 7]

bin_names = ['4-5', '5-6', '6-7']

legend = ['4-5', '5-6', '6-7']

fig, ax = plt.subplots()
# Create a histogram which divides the data into 10 bins.
ax.hist(selected, bins=bins, label=bin_names, linewidth=1, edgecolor="green", color='red')

# Add the horizontal grid lines.
ax.grid(axis="y")

ax.legend()

plt.xlabel('Length')
plt.ylabel('Frequency')

# Display the Figure.
plt.show()




