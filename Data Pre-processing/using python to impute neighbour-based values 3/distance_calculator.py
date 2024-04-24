# distance_calculator.py
import math


def calculate_distance(first, second):
    total = 0
    for a, b in zip(first, second):
        if a.strip() != "" and b.strip() != "":
            total += math.pow(float(a) - float(b), 2)

    return math.sqrt(total)
