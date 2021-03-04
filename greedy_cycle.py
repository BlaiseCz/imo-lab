from copy import deepcopy

def greedy_cycle_propose(distance_matrix, visited, current_cycle):

    # current_node = distance_matrix[start_with]
    # first_nearest_node_dist = sorted(current_node)[1]
    # first_nearest_node_id = current_node.index(first_nearest_node_dist)

    # cycle.append(first_nearest_node_id)

    visited_node = 0
    if len(current_cycle) == 1:
        current_node = distance_matrix[current_cycle[0]]
        first_nearest_node_dist = sorted(current_node)[1]
        first_nearest_node_id = current_node.index(first_nearest_node_dist)

        cycle = [current_cycle[0]]
        cycle.append(first_nearest_node_id)
        visited_node = first_nearest_node_id

    else:
        cycle = find_node_closest_to_current_cycle(current_cycle, distance_matrix,
                                                   visited=visited)
        for i, node in enumerate(cycle):
            if i >= len(current_cycle) or node != current_cycle[i]:
                visited_node = node
                break



    return cycle, visited_node

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


def find_node_closest_to_current_cycle(current_cycle, distance_matrix,
                                       visited=[]):
    nodes_calculated_cycles = []

    for node_id in range(len(distance_matrix)):
        if (node_id not in current_cycle) and (node_id not in visited):
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
