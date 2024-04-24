# neighbours_finder.py
from data_point import DataPoint
from distance_calculator import calculate_distance

def find_neighbours(target, data, k_value):
    neighbours = list()
    data_with_distances = list()

    for current in data:
        if current != target and any(value.strip() == "" for value in current):
            data_with_distances.append(DataPoint(current, calculate_distance(target, current)))

    while len(neighbours) < k_value and data_with_distances:
        min_distance = float('inf')
        index = -1
        for i in range(len(data_with_distances)):
            if data_with_distances[i].distance < min_distance:
                min_distance = data_with_distances[i].distance
                index = i

        neighbours.append(data_with_distances[index].tuple)
        data_with_distances.pop(index)

    return neighbours
