# imputation.py
from neighbours_finder import find_neighbours
from average_tuple import generate_average_tuple

def impute_missing_values(data, k_value, decimal_digits=1):
    for i in range(0, len(data)):
        if any(value.strip() == "" for value in data[i]):
            neighbours = find_neighbours(data[i], data, k_value)

            # Check if there are neighbors before calculating the average tuple
            if neighbours:
                average_tuple = generate_average_tuple(neighbours)
                for j in range(0, len(data[i])):
                    if data[i][j].strip() == "":
                        format_string = "{0:." + str(decimal_digits) + "f}"
                        data[i][j] = format_string.format(float(average_tuple[j]))
