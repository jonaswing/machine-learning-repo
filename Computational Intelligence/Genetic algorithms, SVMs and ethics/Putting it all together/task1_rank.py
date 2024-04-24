import random
import numpy as np


def create_reference_solution(chromosome_length):
    number_of_ones = int(chromosome_length / 2)

    # Build an array with an equal mix of zero and ones
    reference = np.zeros(chromosome_length)
    reference[0: number_of_ones] = 1

    # Shuffle the array to mix the zeros and ones
    np.random.shuffle(reference)

    return reference


def create_starting_population(individuals, chromosome_length):
    # Set up an initial array of all zeros
    population = np.zeros((individuals, chromosome_length))
    # Loop through each row (individual)
    for i in range(individuals):
        # Choose a random number of ones to create
        ones = random.randint(0, chromosome_length)
        # Change the required number of zeros to ones
        population[i, 0:ones] = 1
        # Shuffle row
        np.random.shuffle(population[i])

    return population


def calculate_fitness(reference, population):
    # Each row in the population is compared to the reference element by element.
    # For each row, this results in a row of True or False values.  True when the
    # values match and False when they don't.
    identical_to_reference = population == reference

    # For each row in identical_to_reference, it sums the values.  True being equal
    # to 1 in this case.  The sum of each row is then divided by the total length of
    # reference solution to give each row a score in the range 0 to 1.
    fitness_scores = identical_to_reference.sum(axis=1) / len(reference)

    # Return the array of calculated scores for the population.
    return fitness_scores


def select_individual_by_rank(population, scores):
    # Determine the initial size of the population using the length
    # of the scores array.
    population_size = len(scores)

    # Rank the population based on their fitness scores.
    ranked_indices = sorted(range(population_size), key=lambda x: scores[x])

    # Assign probabilities based on rank.
    # Higher ranks get higher probabilities.
    selection_probabilities = [1 / (population_size - i) for i in range(population_size)]

    # Randomly select an individual based on rank.
    selected_index = random.choices(ranked_indices, weights=selection_probabilities, k=1)[0]

    # Return the chromosome of the selected individual.
    # This is done by retrieving all of the columns from the selected individual's row
    # in the population.
    return population[selected_index, :]


def breed_by_one_point_crossover(parent_1, parent_2):
    # Determine the length of the chromosome
    chromosome_length = len(parent_1)

    # Randomly select a crossover point (index).
    # The first and last element of the chromosomes are excluded
    # as they will not allow for proper crossover to occur.
    crossover_point = random.randint(1, chromosome_length - 1)

    # The first child is created by using hstack to add the
    # elements of the second parent's chromosome
    # extending from the crossover_point to
    # its end to the elements of the first parent
    # extending from its first element to right before the crossover_point.
    child_1 = np.hstack((parent_1[0:crossover_point],
                         parent_2[crossover_point:]))

    # The second child is created by using hstack to add the
    # elements of the first parent's chromosome
    # extending from the crossover_point to
    # its end to the elements of the second parent
    # extending from its first element to right before the crossover_point.
    child_2 = np.hstack((parent_2[0:crossover_point],
                         parent_1[crossover_point:]))

    # Return the two newly bred children.
    return child_1, child_2


def randomly_mutate_population(population, mutation_probability):
    # Create an array of random numbers, matching the shape of the population.
    # This means a random number will be generated for every gene (column)
    # in every row (individual/chromosome) in the population.
    random_mutation_array = np.random.random(size=(population.shape))

    # Compare the randomly generated value for each gene
    # with the mutation_probability value.
    # If the value is smaller or equal to the mutation_probability a value of True
    # is stored in the new random_mutation_boolean array.  Otherwise
    # a value of False is stored.
    # This will serve as a mask.  Only genes which have evaluated to True
    # will be mutated.  This is why it's important to choose an appropriate
    # mutation_probability.  Selecting a value that is too low will result in
    # too few mutations and selecting a value that is too high will result in
    # too many mutations.
    random_mutation_boolean = random_mutation_array <= mutation_probability

    # Using the random_mutation_boolean array as an index, serves as a mask.
    # Only those genes (elements) where the value in the Boolean array is True
    # will be modified.
    # np.logical_not performs a logical NOT on the provided value, e.g. NOT True is False.
    # For a binary domain such as this one, this has the effect of flipping the gene value
    # of the selected genes.
    population[random_mutation_boolean] = np.logical_not(population[random_mutation_boolean])

    # Return the mutated population.
    return population


# A function for defining and executing a genetic algorithm,
# based on the received parameter values.
def genetic_algorithm(reference_solution,
                      chromosome_length,
                      population_size,
                      maximum_generation,
                      mutation_probability,
                      fitness_target,
                      best_score_progress):
    # Create the initial population.
    population = create_starting_population(population_size, chromosome_length)

    # Calculate the fitness of each member in the initial population.
    scores = calculate_fitness(reference_solution, population)
    # Selects the highest fitness level from the initial population.
    best_score = max(scores)
    # Outputs the best fitness level from the initial population.
    print("Starting best score: {0:.3f}".format(best_score))
    # Append the best fitness level from the initial population
    # to the list of fitness levels from each generation.
    best_score_progress.append(best_score)
    # Define a variable for keeping track of the current generation (epoch).
    generation = 0

    # This loop drives the GA. In this example it will keep iterating across
    # generations (epochs) until the maximum generation or the required fitness
    # level has been reached.
    while generation < maximum_generation and best_score < fitness_target:
        # Create an empty list to contain the new population.
        new_population = []

        # Create the new population by generating two children at a time.
        # The loop needs to iterate half the times of the required population
        # size, as each iteration will generate two members of the new
        # population.
        for i in range(int(population_size / 2)):
            # Two members from the existing population need to be selected for
            # breeding.  This is accomplished using the select_individual_by_tournament
            # function.  The function is called twice to select the two individuals.
            parent_1 = select_individual_by_rank(population, scores)
            parent_2 = select_individual_by_rank(population, scores)
            # Generate two offspring using the breed_by_one_point_crossover
            # function.
            child_1, child_2 = breed_by_one_point_crossover(parent_1, parent_2)
            # Add the two children to the new population (next generation).
            new_population.append(child_1)
            new_population.append(child_2)

        # Replace the old (current) population with the new one.
        population = np.array(new_population)

        # Mutate the population using the randomly_mutate_population function.
        population = randomly_mutate_population(population, mutation_probability)

        # Calculate the fitness of each member in the new population.
        scores = calculate_fitness(reference_solution, population)
        # Selects the highest fitness level from the new population.
        best_score = max(scores)
        # Outputs the best fitness level from the new population.
        print("Generation {0} fitness: {1:.3f}".format(generation + 1, best_score))
        # Append the best fitness level from the new population
        # to the list of fitness levels from each generation.
        best_score_progress.append(best_score)
        # Increment the generation variable.
        generation += 1

    # Return the fittest solution from the
    # current (final)population, along with its fitness.
    return population[scores.tolist().index(best_score)], best_score


# Define the parameters which define and control the GA.
# The number of genes per chromosome.
chromosome_length = 75
# The number of chromosomes (population members) to
# have in each generation.
population_size = 100
# The maximum number of epochs to iterate over.  The
# GA will stop when the number of epochs is reached,
# regardless of whether the fitness_target was reached.
maximum_generation = 1000
# A value controlling the rate of mutation.  Smaller
# values results in fewer mutations.
mutation_probability = 0.005
# For this example, possible fitness values are in the
# range 0 to 1.  A fitness target of 1 means that the
# best solution in the population should be an exact match
# for the reference solution.
fitness_target = 1,
# An list to track the best score in each generation.  This
# is useful for demonstrating the GA's progress towards
# its goal.
best_score_progress = []

# Creates a reference solution.  Not all GAs will have this step.
# In the real-world this step might be as simple as defining
# what an "optimal" solution is.
reference_solution = create_reference_solution(chromosome_length)

# Calls the genetic_algorithm function with the specified parameters.
# The function returns a tuple consisting of the fittest solution
# and highest fitness.
fittest_solution, best_score = genetic_algorithm(reference_solution,
                                                 chromosome_length,
                                                 population_size,
                                                 maximum_generation,
                                                 mutation_probability,
                                                 fitness_target,
                                                 best_score_progress)

# Output the fittest solution.
print("Fittest solution:\n", fittest_solution)