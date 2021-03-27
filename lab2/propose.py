import itertools
import random
from copy import deepcopy

from lab1.distance_counter import calculate_distance
from lab2.local_search import set_ids_order


def propose_in_route(distance_matrix, cycle1, cycle2):
    # first cycle
    combi1 = list(itertools.combinations(range(len(cycle1)), 2))
    random.shuffle(combi1)
    for i1, i2 in combi1:
        gain1 = switch_nodes(cycle1, distance_matrix, i1, i2)
        gain2 = switch_edges(cycle1, distance_matrix, i1, i2)

        if gain1 > gain2:
            num = 0
            gain = gain1
        else:
            num = 3
            gain = gain2

        yield gain, i1, i2, num

    # second cycle
    combi2 = list(itertools.combinations(range(len(cycle2)), 2))
    random.shuffle(combi2)
    for i1, i2 in combi2:
        gain1 = switch_nodes(cycle2, distance_matrix, i1, i2)
        gain2 = switch_edges(cycle2, distance_matrix, i1, i2)

        if gain1 > gain2:
            num = 1
            gain = gain1
        else:
            num = 4
            gain = gain2

        yield gain, i1, i2, num


def switch_nodes(cycle, distance_matrix, i1, i2):
    gain = 0
    if (i1 - 1) % len(cycle) != i2:
        gain += distance_matrix[cycle[i1]][cycle[(i1 - 1) % len(cycle)]] + \
                distance_matrix[cycle[i2]][cycle[(i2 + 1) % len(cycle)]]
        gain -= distance_matrix[cycle[i1]][cycle[(i2 + 1) % len(cycle)]] + \
                distance_matrix[cycle[i2]][cycle[(i1 - 1) % len(cycle)]]
    if (i2 - 1) % len(cycle) != i1:
        gain += distance_matrix[cycle[i1]][cycle[(i1 + 1) % len(cycle)]] + \
                distance_matrix[cycle[i2]][cycle[(i2 - 1) % len(cycle)]]
        gain -= distance_matrix[cycle[i1]][cycle[(i2 - 1) % len(cycle)]] + \
                distance_matrix[cycle[i2]][cycle[(i1 + 1) % len(cycle)]]
    return gain


def switch_edges(cycle, distance_matrix, i1, i2):
    first_node, second_node = set_ids_order(i1, i2)

    updated_path = deepcopy(cycle)
    updated_path[first_node:second_node] = updated_path[first_node:second_node][::-1]

    gain = 0
    gain += distance_matrix[cycle[first_node]][cycle[(first_node - 1) % len(cycle)]] + \
            distance_matrix[cycle[second_node-1]][cycle[(second_node) % len(cycle)]]

    gain -= distance_matrix[updated_path[first_node]][updated_path[(first_node - 1) % len(cycle)]] + \
            distance_matrix[updated_path[second_node-1]][updated_path[(second_node) % len(cycle)]]

    return gain


def propose_between_routes(distance_matrix, cycle1, cycle2):
    prod = list(itertools.product(range(len(cycle1)), range(len(cycle2))))
    random.shuffle(prod)
    for i1, i2 in prod:
        gain = 0
        gain += distance_matrix[cycle1[i1]][cycle1[(i1 - 1) % len(cycle1)]] + \
                distance_matrix[cycle1[i1]][cycle1[(i1 + 1) % len(cycle1)]] + \
                distance_matrix[cycle2[i2]][cycle2[(i2 - 1) % len(cycle2)]] + \
                distance_matrix[cycle2[i2]][cycle2[(i2 + 1) % len(cycle2)]]

        gain -= distance_matrix[cycle1[i1]][cycle2[(i2 - 1) % len(cycle2)]] + \
                distance_matrix[cycle1[i1]][cycle2[(i2 + 1) % len(cycle2)]] + \
                distance_matrix[cycle2[i2]][cycle1[(i1 - 1) % len(cycle1)]] + \
                distance_matrix[cycle2[i2]][cycle1[(i1 + 1) % len(cycle1)]]
        # returning cycle1 index and cycle2 index to swap
        yield gain, i1, i2, 2
