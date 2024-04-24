# average_tuple.py
def generate_average_tuple(data):
    return_me = [0] * len(data[0])

    # Count the non-empty values for each attribute
    count_non_empty = [0] * len(data[0])

    for current in data:
        for i in range(0, len(current)):
            if current[i].strip() != "":
                return_me[i] += float(current[i])
                count_non_empty[i] += 1

    # Avoid division by zero
    for i in range(0, len(return_me)):
        if count_non_empty[i] > 0:
            return_me[i] = return_me[i] / count_non_empty[i]

    return return_me
