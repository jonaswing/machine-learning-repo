def clipping_normalisation(target):
    normalised = []  # defines a list to store the normalised values
    # Use the max function to find the maximum value in the target list
    max_value = max(target)
    if max_value > 100:
        print("")
    print("Max Value:", max_value)
    # Determine the length in digits of the maximum value, this value
    # will be used to determine by how much any value should be shifted
    # to be beyond the decimal point. By first converting the number to a
    # string (excluding any values beyond the decimal point),
    # the len function can be used to count the number of digits.
    digits = len(str("{0:.0f}".format(max_value)))
    print("Digits:", digits)

    # Apply the normalisation to each item in the target list
    for v in target:
        v_norm = v / pow(10, digits)
        # Adds the normalised value to the normalised list
        normalised.append(v_norm)

    return normalised  # Returns the list of normalised values

def output(original, normalised):
    print('Original\tNormalised')
    for o, n in zip(original, normalised):
        print(f"{o}\t\t{n:.3f}")

if __name__ == '__main__':
    values = [234, 954, 21, 678, 375, 68, 475, 190, 89, 530]

    # Calls the decimal_scaling_normalisation function by passing the list of values
    # to be normalised
    normalised = decimal_scaling_normalisation(values)
    output(values, normalised)