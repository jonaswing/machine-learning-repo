import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
import pandas as pd


# Load the diabetes dataset
diabetes = load_diabetes()

sex = [0,1]
age = [15,18]

fig, ax = plt.subplots()
# Creates a bar plot. The first two parameters passed
# are x and height. In this case, x is provided as a list of string
# values. The bar() function will automatically derive that there are 5
# x-coordinates required as there are 5 values in the list. The 5 values
# will become the tick labels. The sales_numbers are used as the heights
# of the individual bars.
ax.bar(sex, age)
# Add detail to the Axes.
ax.set_title("Age and sex")
ax.set_xlabel("Sex")
ax.set_ylabel("Age")
# Display the Figure.
plt.show()



