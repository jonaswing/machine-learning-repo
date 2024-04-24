import random
import numpy as np

# Step 1: Setup - Generate random initial schedule
def generate_random_schedule(employees, days, shifts_per_day):
    schedule = np.zeros((days, shifts_per_day), dtype=int)
    for day in range(days):
        employee_indices = np.random.permutation(employees)
        for i in range(shifts_per_day):
            schedule[day, i] = employee_indices[i]
    return schedule

# Step 2: Check - Evaluate schedule fitness based on criteria like coverage and fairness
def evaluate_schedule(schedule):
    # For simplicity, let's say higher numbers are better, and our criteria are coverage and fairness
    coverage = np.sum(schedule != 0, axis=0)  # Total number of shifts assigned to each employee
    fairness = np.std(coverage)  # Standard deviation of shifts assigned, lower is better
    return sum(coverage), -fairness  # Combined fitness score

# Step 3: Choose - Select top schedules based on fitness
def select_top_schedules(schedules, top_percent):
    sorted_indices = np.argsort([evaluate_schedule(schedule)[0] for schedule in schedules])[::-1]
    top_indices = sorted_indices[:int(len(schedules) * top_percent)]
    return [schedules[i] for i in top_indices]

# Step 4: Mix - Combine parts of top schedules to create new schedules
def mix_schedules(top_schedules, mutation_rate):
    new_schedules = []
    for _ in range(len(top_schedules)):
        parents = random.sample(top_schedules, 2)
        crossover_point = random.randint(1, len(parents[0]) - 1)
        child = np.vstack((parents[0][:crossover_point], parents[1][crossover_point:]))
        if random.random() < mutation_rate:
            mutation_index = random.randint(0, len(child) - 1)
            employee_index = random.randint(0, len(child[0]) - 1)
            child[mutation_index][employee_index] = 1 - child[mutation_index][employee_index]  # Flip the bit
        new_schedules.append(child)
    return new_schedules

# Step 5: Repeat - Iteratively improve schedules
def optimize_schedule(employees, days, shifts_per_day, population_size, generations, mutation_rate):
    schedules = [generate_random_schedule(employees, days, shifts_per_day) for _ in range(population_size)]
    for _ in range(generations):
        top_schedules = select_top_schedules(schedules, 0.2)
        if not top_schedules:  # Check if the list is empty
            continue  # Skip to the next generation if no schedules are available
        schedules = mix_schedules(top_schedules, mutation_rate)
    if not schedules:  # If all schedules were eliminated, return a random schedule
        return generate_random_schedule(employees, days, shifts_per_day)
    return max(schedules, key=evaluate_schedule)


# Example usage
employees = 5
days = 7
shifts_per_day = 3
population_size = 100
generations = 50
mutation_rate = 0.1

best_schedule = optimize_schedule(employees, days, shifts_per_day, population_size, generations, mutation_rate)
print("Best schedule:\n", best_schedule)
