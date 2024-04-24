import matplotlib.pyplot as plt

# Data
food_items = ['Burgers', 'Hot dogs', 'Pizzas', 'Smoothies', 'Ice cream']
sales_numbers = [52, 27, 91, 47, 32]

# Creating the bar plot
plt.figure(figsize=(10, 6))
plt.bar(food_items, sales_numbers, color='skyblue')

# Adding title and labels
plt.title('Two-day sales report')
plt.xlabel('Food Items')
plt.ylabel('Sales Numbers')

# Save as image
plt.savefig('sales_report.jpg')

# Displaying the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


