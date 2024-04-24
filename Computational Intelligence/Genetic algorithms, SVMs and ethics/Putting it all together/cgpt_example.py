import random


# Step 1: Setup - Get random pizza recipes
def get_random_recipe():
    ingredients = ['dough', 'tomato sauce', 'cheese', 'pepperoni', 'mushrooms', 'onions', 'bell peppers']
    return random.sample(ingredients, random.randint(2, len(ingredients)))


# Step 2: Check - Taste pizzas and rate them
def rate_pizza(recipe):
    # Here, we're just generating a random score for simplicity
    return random.uniform(0, 10)


# Step 3: Choose - Pick the yummiest pizzas
def select_best_pizzas(pizzas, num_best):
    return sorted(pizzas, key=lambda x: x[1], reverse=True)[:num_best]


# Step 4: Mix - Combine parts of tasty pizzas
def mix_recipes(pizzas):
    mixed_recipe = []
    for pizza in pizzas:
        mixed_recipe.extend(pizza[0])
    return mixed_recipe


# Step 5: Change - Sometimes try different ingredients
def mutate_recipe(recipe):
    if random.random() < 0.3:  # 30% chance of mutation
        index_to_change = random.randint(0, len(recipe) - 1)
        new_ingredient = random.choice(['sausage', 'pineapple', 'olives', 'ham', 'chicken'])
        recipe[index_to_change] = new_ingredient
    return recipe


# Step 6: Keep going - Repeat cooking and tasting
def optimize_pizza():
    num_iterations = 10
    num_best_to_select = 3

    # Generate initial random pizzas
    pizzas = [(get_random_recipe(), rate_pizza(get_random_recipe())) for _ in range(num_iterations)]

    for i in range(num_iterations):
        # Step 3: Choose the best pizzas
        best_pizzas = select_best_pizzas(pizzas, num_best_to_select)

        # Step 4: Mix the ingredients of the best pizzas
        mixed_recipe = mix_recipes(best_pizzas)

        # Step 5: Sometimes change ingredients
        mixed_recipe = mutate_recipe(mixed_recipe)

        # Step 2: Check the new pizza
        new_pizza_score = rate_pizza(mixed_recipe)

        # Replace a random pizza with the new one
        pizzas[random.randint(0, num_iterations - 1)] = (mixed_recipe, new_pizza_score)

    # Step 7: Stop - Find the best pizza
    best_pizza = max(pizzas, key=lambda x: x[1])
    return best_pizza


# Step 8: Result - Enjoy the best pizza recipe
best_recipe, best_score = optimize_pizza()
print("Best pizza recipe:", best_recipe)
print("Best pizza score:", best_score)
