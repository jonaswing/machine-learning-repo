import numpy as np
import pandas as pd
from scipy.spatial import distance
from sklearn.preprocessing import MinMaxScaler
import requests


cities = "https://core-noroff.bravais.com/api/dynamic/documentVersions/20078/files/251181/media/AML/Computational%20Intelligence/Other/Cities.txt"

cities = requests.get(cities)

if cities.status_code == 200:
    data = cities.text
    print(data)
else:
    print("Failed to retrieve data. Status code:", cities.status_code)


def load_cities(target_file):
    # Load the target file into a NumPy array.
    cities = np.loadtxt(target_file, dtype=float)
    # Return the loaded cities.
    return cities


def create_starting_population(individuals, chromosome_length):
    # Set up an initial array of all zeros
    population = np.zeros((individuals, chromosome_length))
    # Loop through each row (individual)
    for i in range(individuals):
        # Each city coordinate is associated with a number in cities file.
        # Every gene in the chromosome is set to a number corresponding to a city.
        for j in range(chromosome_length):
            population[i, j] = j + 1

        # Shuffle the city numbers for the specific individual.
        np.random.shuffle(population[i])

    # Return the newly generated population
    return population


def calculate_distance(cities, cityIndexOne, cityIndexTwo):
    # Retrieve only the coordinates (not the city number), for
    # each city and then reshape the array to the required format.
    coord1 = np.reshape(cities[int(cityIndexOne), -2:], (1, 2))
    coord2 = np.reshape(cities[int(cityIndexTwo), -2:], (1, 2))

    # Use the cdist function to calculate the "euclidean" distance
    # between the two city coordinates.
    return distance.cdist(coord1, coord2, "euclidean")

def calculate_fitness(cities, population):
    # Declare a numpy array to store the fitness score of each
    # individual in the population.
    fitness_scores = np.zeros(len(population))

    # Iterate over all the individuals in the population.
    for i in range(len(population)):
        # Calculate the fitness score by summing the distance between each consecutive city,
        # as specified by the individual's gene sequence.
        score = 0
        for j in range(len(population[i]) - 1):
            score += calculate_distance(cities, population[i, j] - 1, population[i, j+1] - 1)
        # Add the distance between the last and first city in the chromosome.
        score += calculate_distance(cities, population[i, len(population[i]) - 1] - 1, population[i, 0] - 1)
        # Add the sum of the path distance as the fitness score for the individual.
        fitness_scores[i] = score

    # Return all the fitness scores.
    return fitness_scores

def sort_population_by_fitness(population, scores):
    # Sort both the population and fitness scores by fitness.
    # The fittest individual will be at index 0 at the end of the sort
    # and the least fit at the highest index.
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(scores) - 1):
            if scores[i] > scores[i + 1]:
                tempscore = scores[i]
                scores[i] = scores[i + 1]
                scores[i + 1] = tempscore
                temppop = population[i]
                population[i] = population[i + 1]
                population[i + 1] = temppop
                swapped = True

    return population, scores

def select_individual(population, scores):
    # Retrieve the best fitness from the scores.
    best = scores[0]
    # For each score, calculate its difference from the best score.
    relative_scores = scores - best
    # Reshape the list of relative_scores into a single-dimensional NumPy array.
    relative_scores = np.reshape(relative_scores, (len(relative_scores), 1))
    # Declare a MinMaxScaler with default settings.
    scaler = MinMaxScaler()
    # Use the scaler to scale the relative scores onto a set scale.
    relative_scores = pd.DataFrame(scaler.fit_transform(relative_scores)).values
    # Generate a random value in the range 0 to 0.75 to serve as a threshold for picking members of the
    # population.  Other values may be specified here to
    threshold = np.random.random() * 0.75

    # Attempt to find an individual with a relative score higher
    # than the threshold value.  As many attempts will be made as there are
    # individuals in the population.
    for i in range(len(scores)):
        # Test if the current individual is above the threshold.
        if relative_scores[i] > threshold:
            return population[i]

    # If no individual was selected by the loop above, return the best performing individual
    # from the current population.
    return population[0]

def breed_by_multi_point_crossover(parent_1, parent_2):

    # Calculate two points at which to crossover
    firstpoint = int(np.random.random() * (len(parent_1) - 1))
    secondpoint = int(np.random.random() * (len(parent_1) - 1))

    while firstpoint == secondpoint:
        secondpoint = int(np.random.random() * (len(parent_1) - 1))

    # Ensure the two points are in sequence.
    firstcut = 0
    secondcut = 0

    if firstpoint < secondpoint:
        firstcut = firstpoint
        secondcut = secondpoint
    else:
        firstcut = secondpoint
        secondcut = firstpoint

    # Create children by copying genes selectively from
    # the two parents, depending on between which crossover
    # points the current intdex is.
    child_1 = np.zeros(parent_1.shape)
    child_2 = np.zeros(parent_2.shape)

    for i in range(len(child_1)):
        if i >= firstcut and i <= secondcut:
            child_1[i] = parent_1[i]
            child_2[i] = parent_2[i]

    Index = secondcut + 1

    for i in range(len(parent_2)):
        if parent_2[i] not in child_1:
            child_1[Index] = parent_2[i]
            Index += 1
        if Index == len(parent_2):
            Index = 0

    Index = secondcut + 1

    for i in range(len(parent_1)):
        if parent_1[i] not in child_2:
            child_2[Index] = parent_1[i]
            Index += 1
        if Index == len(parent_1):
            Index = 0

    # Return children
    return child_1, child_2


def randomly_mutate_population(population, mutation_probability):
    # Iterate over the entire population.
    for i in range(len(population)):
        # Test if a random value is smaller than the mutation_probability.
        while np.random.random() < mutation_probability:
            # If it is, perform a swap.
            firstcity = int(np.random.random() * (len(population[i]) - 1))
            secondcity = int(np.random.random() * (len(population[i]) - 1))
            swap = population[i, firstcity]
            population[i, firstcity] = population[i, secondcity]
            population[i, secondcity] = swap

    # Return the mutated population.
    return population

# A function for defining and executing a genetic algorithm,
# based on the received parameter values.
def genetic_algorithm(cities,
                     chromosome_length,
                     population_size,
                     maximum_generation,
                     mutation_probability,
                     threshold,
                     no_mutations_threshold,
                     no_improvement_multiplier,
                     best_score_progress):
    # Set the current_mutation_probability and current_population_size.
    # These variables are used to
    # vary the mutation rate  and population size if no improvement has
    # been seen for the
    # number of generations set in the no_mutations_threshold variable.
    current_mutation_probability = mutation_probability
    current_population_size = population_size

    # Create the initial population.
    population = create_starting_population(current_population_size, chromosome_length)

    # Calculate the fitness of each member in the initial population.
    scores = calculate_fitness(cities, population)
    # Sorts the population and fitness scores by fitness value.
    population, scores = sort_population_by_fitness(population, scores)
    # Selects the highest fitness level from the initial population.
    best_score = min(scores)
    # Outputs the best fitness level from the initial population.
    print ("Starting best score: {0:.3f}".format(best_score))
    # Append the best fitness level from the initial population
    # to the list of fitness levels from each generation.
    best_score_progress.append(best_score)
    # Define a variable for keeping track of the current generation (epoch).
    generation = 0
    # Tracks the generation in which the best fitness was found.
    fittest_generation = generation
    # Define a variable for keeping track of the number of generations with no improvement.
    no_improvement = 0

    # This loop drives the GA. In this example it will keep iterating across
    # generations (epochs) until the maximum generation or the required fitness
    # level has been reached.
    while generation < maximum_generation and no_improvement < threshold:

        # Create an empty list to contain the new population.
        new_population = []

        # Add the top performing 10 % of the previous generation to the new generation.
        # This ensures that the optimal solutions are always retained into the next
        # generation.
        for i in range(int(current_population_size / 10)):
            new_population.append(population[int(i)])
    
        # Create the new population by generating two children at a time.
        # The loop needs to iterate half the times of the required population
        # size, as each iteration will generate two members of the new
        # population.
        while len(new_population) < current_population_size:
           # Two members from the existing population need to be selected for
           # breeding.  This is accomplished using the select_individual_by_tournament
           # function.  The function is called twice to select the two individuals.
           parent_1 = select_individual(population, scores)
           parent_2 = select_individual(population, scores)
           # Generate two offspring using the breed_by_one_point_crossover
           # function.
           child_1, child_2 = breed_by_multi_point_crossover(parent_1, parent_2)
           # Add the two children to the new population (next generation).
           new_population.append(child_1)
           new_population.append(child_2)
    
        # Replace the old (current) population with the new one.
        population = np.array(new_population)

        # Mutate the population using the randomly_mutate_population function.
        population = randomly_mutate_population(population,current_mutation_probability)

        # Calculate the fitness of each member in the new population.
        scores = calculate_fitness(cities, population)
        # Sorts the population and fitness scores by fitness value.
        population, scores = sort_population_by_fitness(population, scores)
        # Selects the highest fitness level from the new population.
        best_score = min(scores)
        # Outputs the best fitness level from the new population.
        print("No improvement in {0} generation(s). Mutation probability: {1}.  Population size: {2}. Generation {3} fitness: {4:.3f} ({5})".format(
                                                                                         no_improvement, current_mutation_probability,
                                                                                         current_population_size,
                                                                                         generation, best_score, fittest_generation))
        # Append the best fitness level from the new population
        # to the list of fitness levels from each generation.

        # Check whether there was an improvement.
        if best_score < min(best_score_progress):
            # If there was, reset all variables.
            no_improvement = 0
            current_mutation_probability = mutation_probability
            current_population_size = population_size
            # Update the ShortestEverPath to reflect the new best path.
            ShortestEverPath = population[0]
            # Tracks the generation in which the best fitness was found.
            fittest_generation = generation
        else:
            no_improvement += 1
            # Test how many generations have passed with no change and adjust the mutation
            # probability if necessary.
            if no_improvement % no_mutations_threshold == 0:
                current_mutation_probability = current_mutation_probability * no_improvement_multiplier

                # Cap the mutation rate at 0.5
                if current_mutation_probability > 0.5:
                    current_mutation_probability = 0.5

                current_population_size = int(current_population_size * no_improvement_multiplier)

        best_score_progress.append(best_score)
        # Increment the generation variable.
        generation += 1

    # Return the fittest solution from the
    # current (final)population, along with its fitness.
    return population[scores.tolist().index(best_score)], best_score

# Call the load_cities function to load the cities
# into a NumPy array.
cities = load_cities("cities.txt")
# Set the chromosome length to be the number of cities,
# since each city should be included in the path once.
chromosome_length = len(cities)
# The number of chromosomes (population members) to
# have in each generation.  This value may be varied
# by experimentation.  Ensure it is higher than the
# number of cities.
population_size = len(cities) * 5
# The maximum number of epochs to iterate over.
# For this example there is no maximum fitness so the GA
# will run until this number of epochs have been reached
# or there has been no improvement for the number of
# epochs as specified in the threshold variable.
maximum_generation = 100000
# A value controlling the rate of mutation.  Smaller
# values results in fewer mutations.
mutation_probability = 0.005
# The GA will stop if there has been no improvement for the
# number of epochs specified in the threshold.
threshold = 500
# The GA will increase it's mutation probability if the
# number of generations specified by the no_mutations_threshold
# variable.
no_mutations_threshold = 50
# Multiplier to multiply the mutation_probability and population_size with whenever
# the no_mutations_threshold is reached.  Using a variable population size
# and mutation_probability avoids the solution becoming stuck in a local
# minimum.
no_improvement_multiplier = 1.5
# An list to track the best score in each generation.  This
# is useful for demonstrating the GA's progress towards
# its goal.
best_score_progress = []

# Calls the genetic_algorithm function with the specified parameters.
# The function returns a tuple consisting of the fittest solution
# and highest fitness.
fittest_solution, best_score = genetic_algorithm(cities,
                                chromosome_length,
                                population_size,
                                maximum_generation,
                                mutation_probability,
                                threshold,
                                no_mutations_threshold,
                                no_improvement_multiplier,
                                best_score_progress)

# Output the fittest solution.
print("Fittest solution:\n", fittest_solution)