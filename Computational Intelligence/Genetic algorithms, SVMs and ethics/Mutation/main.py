
import random
import numpy as np

def create_reference_solution(chromosome_length):

    # Determine how many ones should be generated.
    number_of_ones = int(chromosome_length / 2)

    # Build an array with an equal mix of zeroes and ones,
    # by first filling the entire array with zeroes.
    reference = np.zeros(chromosome_length)
    # The first half of the array is then filled with ones.
    reference[0: number_of_ones] = 1

    # Lastly, the array is shuffled to have a mix of ones and zeroes.
    np.random.shuffle(reference)

    # The reference array is returned.
    return reference


def create_starting_population(individuals, chromosome_length):
    # Set up an initial multidimensional array of all zeroes.
    # The number of rows in the array corresponds to the number of
    # required individuals in the population.
    # The number of columns corresponds to the required chromosome length.
    population = np.zeros((individuals, chromosome_length))
    # Loop through each row (individual) in the array.
    for i in range(individuals):
        # Choose a random number of ones to create.
        ones = random.randint(0, chromosome_length)
        # Change the required number of zeroes to ones.
        population[i, 0:ones] = 1
        # Shuffle the row
        np.random.shuffle(population[i])

    # Return the newly created population.
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


def select_individual_by_tournament(population, scores):
    # Determine the initial size of the population using the length
    # of the scores array.
    population_size = len(scores)

    # Randomly generate indices to select two "fighters"
    # from the population to take part in the tournament.
    fighter_1 = random.randint(0, population_size - 1)
    fighter_2 = random.randint(0, population_size - 1)

    # For each of the two fighters, use the index to retrieve
    # their fitness from the scores array.
    fighter_1_fitness = scores[fighter_1]
    fighter_2_fitness = scores[fighter_2]

    # Compare the fitness of the two fighters.  The one
    # with the highest fitness is the winner.
    if fighter_1_fitness >= fighter_2_fitness:
        winner = fighter_1
    else:
        winner = fighter_2

    # Return the chromosome of the winning fighter.
    # This is done by retrieving all of the columns from the winner's row
    # in the population.
    return population[winner, :]


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
    # This will serve as a mask.  Only genes that have evaluated to True
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