from copy import deepcopy
from distance_counter import calculate_distance
from random import sample


def k_regret_connector(algos, distance_matrix, k=1):
    cycles = sample(list(range(len(distance_matrix))), len(algos))
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
    return history


def turns_connector(algos, distance_matrix):
    cycles = sample(list(range(len(distance_matrix))), len(algos))
    cycles = [[c] for c in cycles]
    visited = []
    for c in cycles:
        visited += c

    history = [deepcopy(cycles)]

    while len(visited) != len(distance_matrix):
        for ai, algo in enumerate(algos):
            cycle, visited_node = algo(distance_matrix, visited, cycles[ai])
            cycles[ai] = cycle
            history.append(deepcopy(cycles))
            visited.append(visited_node)
    return history
