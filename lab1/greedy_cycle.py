from copy import deepcopy
import math


def greedy_cycle_propose(distance_matrix, visited, current_cycle):
    mini = int(10e20)
    chosen_point = -1
    chosen_place = -1
    for i, node in enumerate(current_cycle):
        for ip, point in enumerate(distance_matrix):
            if ip in visited:
                continue
            dist_added = distance_matrix[current_cycle[i - 1]][ip] + distance_matrix[node][ip] \
                         - distance_matrix[current_cycle[i - 1]][node]

            if dist_added < mini:
                mini = dist_added
                chosen_point = ip
                chosen_place = i
    res_cycle = deepcopy(current_cycle)
    # res_cycle = current_cycle
    res_cycle.insert(chosen_place, chosen_point)
    return res_cycle, chosen_point


def greedy_cycle(distance_matrix, start_with):
    cycle = [start_with]
    history = [cycle]

    current_node = distance_matrix[start_with]
    first_nearest_node_dist = sorted(current_node)[1]
    first_nearest_node_id = current_node.index(first_nearest_node_dist)

    cycle.append(first_nearest_node_id)
    history.append(deepcopy(cycle))

    while not len(cycle) == len(distance_matrix):
        cycle = find_node_closest_to_current_cycle(cycle, distance_matrix)
        history.append(deepcopy(cycle))

    print(f'dist: {calculate_dist_of_given_cycle(cycle, distance_matrix)}')
    return cycle, history


def find_node_closest_to_current_cycle(current_cycle, distance_matrix):
    nodes_calculated_cycles = []

    for node_id in range(len(distance_matrix)):
        if node_id not in current_cycle:
            nodes_calculated_cycles.append(calculate_dist_with_new_node(current_cycle, node_id, distance_matrix))

    best_match_cycle = min(nodes_calculated_cycles, key=lambda x: x['path_dist'])
    return best_match_cycle['cycle']


def calculate_dist_with_new_node(cycle, node_to_add, distance_matrix):
    best_path_cycle_dict = []

    for x in range(len(cycle) + 1):
        updated_cycle = deepcopy(cycle)
        updated_cycle.insert(x, node_to_add)

        best_path_cycle_dict.append(
            {
                'node_to_dad': node_to_add,
                'path_dist': calculate_dist_of_given_cycle(updated_cycle, distance_matrix),
                'cycle': updated_cycle
            })

    return min(best_path_cycle_dict, key=lambda x: x['path_dist'])


def calculate_dist_of_given_cycle(cycle, distance_matrix):
    dist = 0

    for x in range(len(cycle) - 1):
        dist += distance_matrix[cycle[x]][cycle[x + 1]]

    return dist
