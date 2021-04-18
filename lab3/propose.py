import itertools
import random
import numpy as np
from copy import deepcopy

from lab2.local_search import set_ids_order

def propose_nodes_switch(distance_matrix, cycle1: list, cycle2: list,
                         fresh=set()):
    # jeżeli sprawdzamy wszystkie wierzchołki
    if not fresh:
        proposer = itertools.combinations(cycle1 + cycle2, 2)
    # jeżeli proponujemy tylko z częścią wierzchołków (zamienione i ich sąsiedzi)
    # do fresh dodawaj numery wierzchołków a nie indeksy w tablicy!
    else:
        proposer = itertools.product(fresh, set(cycle1+cycle2) - fresh)

    for node1, node2 in proposer:
        # sprawdzamy w których cyklach są wybrane node'y
        where = []
        if node1 in cycle1:
            i1 = cycle1.index(node1)
            where.append(0)
        else:
            i1 = cycle2.index(node1)
            where.append(1)

        if node2 in cycle1:
            i2 = cycle1.index(node2)
            where.append(0)
        else:
            i2 = cycle2.index(node2)
            where.append(1)

        # liczymy gaina z zamiany
        # wierzchołki są w różnych cyklach
        if where == [1,0]:
            # chcemy mieć najpierw cykl1, potem cykl2
            node1, node2 = node2, node1
            i1, i2 = i2, i1
            where = [0,1]

        if where == [0,1]:
            num = 2
            gain = gain_switch_nodes_between(distance_matrix, cycle1, cycle2, i1,i2)

        # oba wierzchołki są w tym samym cyklu
        else:
            # oba wierzchołki są w cycle1
            if where[0] == 0:
                gain = switch_edges(cycle1, distance_matrix, i1, i2)
                num = 0
            # oba wierzchołki są w cycle2
            else:
                gain = switch_edges(cycle2, distance_matrix, i1, i2)
                num = 1

        yield gain, i1, i2, num

def propose_in_route(distance_matrix, cycle1, cycle2):
    # first cycle
    combi1 = list(itertools.combinations(range(len(cycle1)), 2))
    random.shuffle(combi1)
    for i1, i2 in combi1:
        gain1 = gain_switch_nodes(cycle1, distance_matrix, i1, i2)
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
        gain1 = gain_switch_nodes(cycle2, distance_matrix, i1, i2)
        gain2 = switch_edges(cycle2, distance_matrix, i1, i2)

        if gain1 > gain2:
            num = 1
            gain = gain1
        else:
            num = 4
            gain = gain2

        yield gain, i1, i2, num


def gain_switch_nodes(cycle, distance_matrix, i1, i2):
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

def gain_switch_nodes_between(distance_matrix, cycle1, cycle2, i1, i2):
    gain = 0
    gain += distance_matrix[cycle1[i1]][cycle1[(i1 - 1) % len(cycle1)]] + \
            distance_matrix[cycle1[i1]][cycle1[(i1 + 1) % len(cycle1)]] + \
            distance_matrix[cycle2[i2]][cycle2[(i2 - 1) % len(cycle2)]] + \
            distance_matrix[cycle2[i2]][cycle2[(i2 + 1) % len(cycle2)]]

    gain -= distance_matrix[cycle1[i1]][cycle2[(i2 - 1) % len(cycle2)]] + \
            distance_matrix[cycle1[i1]][cycle2[(i2 + 1) % len(cycle2)]] + \
            distance_matrix[cycle2[i2]][cycle1[(i1 - 1) % len(cycle1)]] + \
            distance_matrix[cycle2[i2]][cycle1[(i1 + 1) % len(cycle1)]]
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
    gains = np.zeros(len(prod))
    i1s = np.zeros(len(prod))
    i2s = np.zeros(len(prod))
    for idx, (i1, i2) in enumerate(prod):
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
        gains[idx] = gain
        i1s[idx] = i1
        i2s[idx] = i2
    return gains, i1s, i2s, 2

