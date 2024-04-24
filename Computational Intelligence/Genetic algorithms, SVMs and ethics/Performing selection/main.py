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