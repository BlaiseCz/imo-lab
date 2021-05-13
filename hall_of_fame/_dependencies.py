from copy import deepcopy
from .distance import calculate_distance
from random import sample


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
def k_regret_connector(algos, distance_matrix, start_with=None, k=1):
    cycles = sample(list(range(len(distance_matrix))), len(algos))

    if start_with is not None:
        cycles = start_with
    picked_nodes = deepcopy(cycles)

    cycles = [[c] for c in cycles]
    visited = []
    for c in cycles:
        visited += c

    history = [deepcopy(cycles)]
    enough = []

    while sum([len(c) for c in cycles]) < len(distance_matrix):
        min_regret = int(10e20)
        best_algo = -1
        for i, algo in enumerate(algos):
            if i in enough:
                continue
            best_cycle, best_node = algo(distance_matrix, visited, cycles[i])
            best_cost = calculate_distance(distance_matrix, best_cycle) - calculate_distance(distance_matrix, cycles[i])
            regret = 0
            sub_visited = visited + [best_node]
            for ik in range(k - 1):
                sub_cycle, sub_node = algo(distance_matrix, sub_visited,
                                           cycles[i])
                sub_cost = calculate_distance(distance_matrix, sub_cycle) - calculate_distance(distance_matrix,
                                                                                               cycles[i])
                regret += sub_cost - best_cost
                sub_visited.append(sub_node)
            if regret < min_regret:
                min_regret = regret
                best_algo = i
        res_cycle, res_node = algos[best_algo](distance_matrix, visited,
                                               cycles[best_algo])
        cycles[best_algo] = deepcopy(res_cycle)
        visited.append(res_node)
        history.append(deepcopy(cycles))
        if len(cycles[best_algo]) >= len(distance_matrix) // len(cycles) \
                and len(enough) + 1 != len(cycles):
            enough.append(best_algo)
    return history, picked_nodes
