import matplotlib.pyplot as plt

# Defines the data for the bar plot.
food_types = ["Burgers", "Hot dogs", "Pizzas", "Smoothies", "Ice-creams"]
sales_numbers = [52, 27, 91, 47, 32]

fig, ax = plt.subplots()
# Creates a bar plot. The first two parameters passed
# are x and height. In this case, x is provided as a list of string
# values. The bar() function will automatically derive that there are 5
# x-coordinates required as there are 5 values in the list. The 5 values
# will become the tick labels. The sales_numbers are used as the heights
# of the individual bars.
ax.bar(food_types, sales_numbers)
# Add detail to the Axes.
ax.set_title("Sales of food types for the last month")
ax.set_xlabel("Food type")
ax.set_ylabel("Number of sales")
# Display the Figure.
plt.show()