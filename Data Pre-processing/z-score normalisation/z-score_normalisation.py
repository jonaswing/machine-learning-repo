import math

def standard_deviation(target):
    # Use the sum and len functions to find the mean of the target list
    mean_value = sum(target) / len(target)

    # Find the squared deviation (difference) of each of the values in the target list
    # from the mean and add it to a running total
    total = 0
    for current in target:
        total += pow(current - mean_value, 2)

    # Divide the total by the number of items in the original list to arrive
    # at the variance of the data set
    variance = total / len(target)
    # Calculate the standard deviation by finding the square root of the variance
    std_dev = math.sqrt(variance)
    # Return the calculated standard deviation
    return std_dev

def z_score_normalisation(target):
    normalised = [] # defines a list to store the normalised values
    # Use the sum and len functions to find the mean of the target list
    mean_value = sum(target) / len(target)
    # Use the standard_deviation function to calculate the standard deviation
    # of the list
    std_dev = standard_deviation(target)

    # Apply the normalisation to each item in the target list
    for v in target:
        v_norm = (v - mean_value) / std_dev
        # Adds the normalised value to the normalised list
        normalised.append(v_norm)

    return normalised # Returns the list of normalised values

def output(original, normalised):
    print('Original\tNormalised')
    for o, n in zip(original, normalised):
        print(f"{o}\t\t{n:.3f}")

if __name__ == '__main__':
    values = [234, 954, 21, 678, 375, 68, 475, 190, 89, 530]

    # Calls the z_score_normalisation function by passing the list of values
    # to be normalised
    normalised = z_score_normalisation(values)
    output(values, normalised)
