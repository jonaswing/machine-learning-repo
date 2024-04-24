def min_max_normalisation(target, new_min, new_max):
    normalised = []
    min_value = min(target)
    max_value = max(target)

    for v in target:
        v_norm = ((v - min_value) / (max_value - min_value)) * (new_max - new_min) + new_min
        # Adds the normalised value to the normalised list
        normalised.append(v_norm)

    return normalised


def output(original, normalised):
    print('Original\tNormalised')
    for o, n in zip(original, normalised):
        print(f"{o}\t\t{n:.3f}")

if __name__ == '__main__':
    values = [346, 94, 235, 855, 775, 65, 75, 765, 39, 643]

    # Calls the min_max_normalisation function by passing the list of values
    # to be normalised, as well as the new range of 0 to 1
    normalised = min_max_normalisation(values, 0, 100)
    output(values, normalised)