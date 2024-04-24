def min_max_normalisation(target, new_min, new_max):
    normalised = []  # defines a list to store the normalised values
    # Use the min function to find the minimum value in the target list
    min_value = min(target)
    # Use the max function to find the minimum value in the target list
    max_value = max(target)

    # Apply the normalisation to each item in the target list
    for v in target:
        v_norm = ((v - min_value) / (max_value - min_value)) * (new_max - new_min) + new_min
        # Adds the normalised value to the normalised list
        normalised.append(v_norm)

    return normalised  # Returns the list of normalised values


def output(original, normalised):
    # Prints the original and normalised values in the specified format
    print("Original\tNormalised")
    for o, n in zip(original, normalised):
        print(f"{o}\t\t{n:.3f}")


if __name__ == '__main__':
    values = [234, 954, 21, 678, 375, 68, 475, 190, 89, 530]

    # Calls the min_max_normalisation function by passing the list of values
    # to be normalised, as well as the new range of 0 to 1
    normalised = min_max_normalisation(values, 0, 1)
    output(values, normalised)
