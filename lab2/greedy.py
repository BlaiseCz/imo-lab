from copy import deepcopy
from random import sample

from lab1.distance_counter import calculate_distance
from lab2.propose import propose_between_routes, propose_in_route


# def greedy(distance_matrix, cycle1, cycle2, propose_method, history):
#     while True:
#         for cost, i1, i2, num in propose_method(distance_matrix, cycle1, cycle2):
#             if cost > 0:
#                 if num == 0:
#                     cycle1[i1], cycle1[i2] = cycle1[i2], cycle1[i1]
#                     history.append(deepcopy([cycle1, cycle1]))
#                 elif num == 1:
#                     cycle2[i1], cycle2[i2] = cycle2[i2], cycle2[i1]
#                     history.append(deepcopy([cycle1, cycle1]))
#                 elif num == 2:
#                     # cycle1[i1], cycle2[i2] = cycle1[i2], cycle2[i1]
#                     cycle1[i1], cycle2[i2] = cycle2[i2], cycle1[i1]
#                     history.append(deepcopy([cycle1, cycle1]))
#
#                 break
#         else:
#             break
#     return cycle1, cycle2, history


def greedy_edges(path, distance_matrix, swap=6):
    better_solution = True
    better_solution_found = False
    best_path = deepcopy(path)
    buff_path = deepcopy(path)
    best_dist = calculate_distance(distance_matrix, path)

    history = [deepcopy(path)]

    while better_solution:
        starting_random_nodes = sample(list(range(len(distance_matrix))), 50)

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


def greedy_nodes(path, distance_matrix):
    better_solution = True
    better_solution_found = False
    best_path = deepcopy(path)
    buff_path = deepcopy(path)
    best_dist = calculate_distance(distance_matrix, path)

    history = [deepcopy(path)]

    while better_solution:
        node_to_switch = sample(list(range(len(distance_matrix))), 2)

        buff_path[node_to_switch[0]], buff_path[node_to_switch[1]] = buff_path[node_to_switch[1]], buff_path[
            node_to_switch[0]]
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
