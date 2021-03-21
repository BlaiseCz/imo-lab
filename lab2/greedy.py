from copy import deepcopy
from random import sample
import numpy as np

from lab1.distance_counter import calculate_distance


def greedy_edges(path, distance_matrix, swap=2):
    better_solution = True
    better_solution_found = False
    best_path = deepcopy(path)
    buff_path = deepcopy(path)
    best_dist = calculate_distance(distance_matrix, path)

    history = [deepcopy(path)]

    while better_solution:
        starting_random_nodes = sample(list(range(len(distance_matrix))), 100)

        for node in starting_random_nodes:
            buff_path[node:swap + node] = buff_path[node:swap + node][::-1]
            updated_dist = calculate_distance(distance_matrix, buff_path)

            if updated_dist < best_dist:
                best_dist = updated_dist
                best_path = buff_path
                print(f'best dist = {best_dist}')
                better_solution_found = True
                history.append(deepcopy(best_path))
        if not better_solution_found:
            better_solution = False

    return best_path, best_dist, history
