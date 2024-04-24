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