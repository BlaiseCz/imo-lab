import itertools
import random


def propose_in_route(distance_matrix, cycle1, cycle2):
    # first cycle
    combi1 = list(itertools.combinations(range(len(cycle1)), 2))
    random.shuffle(combi1)
    for i1, i2 in combi1:
        gain = 0
        gain += distance_matrix[cycle1[i1]][cycle1[(i1 - 1) % len(cycle1)]] + \
                distance_matrix[cycle1[i1]][cycle1[(i1 + 1) % len(cycle1)]] + \
                distance_matrix[cycle1[i2]][cycle1[(i2 - 1) % len(cycle1)]] + \
                distance_matrix[cycle1[i2]][cycle1[(i2 + 1) % len(cycle1)]]

        gain -= distance_matrix[cycle1[i1]][cycle1[(i2 - 1) % len(cycle1)]] + \
                distance_matrix[cycle1[i1]][cycle1[(i2 + 1) % len(cycle1)]] + \
                distance_matrix[cycle1[i2]][cycle1[(i1 - 1) % len(cycle1)]] + \
                distance_matrix[cycle1[i2]][cycle1[(i1 + 1) % len(cycle1)]]
        # returning cycle indexes to swap
        yield gain, i1, i2, 0

    # second cycle
    combi2 = list(itertools.combinations(range(len(cycle2)), 2))
    random.shuffle(combi2)
    for i1, i2 in combi2:
        gain = 0
        gain += distance_matrix[cycle2[i1]][cycle2[(i1 - 1) % len(cycle2)]] + \
                distance_matrix[cycle2[i1]][cycle2[(i1 + 1) % len(cycle2)]] + \
                distance_matrix[cycle2[i2]][cycle2[(i2 - 1) % len(cycle2)]] + \
                distance_matrix[cycle2[i2]][cycle2[(i2 + 1) % len(cycle2)]]

        gain -= distance_matrix[cycle2[i1]][cycle2[(i2 - 1) % len(cycle2)]] + \
                distance_matrix[cycle2[i1]][cycle2[(i2 + 1) % len(cycle2)]] + \
                distance_matrix[cycle2[i2]][cycle2[(i1 - 1) % len(cycle2)]] + \
                distance_matrix[cycle2[i2]][cycle2[(i1 + 1) % len(cycle2)]]
        # returning cycle indexes to swap
        yield gain, i1, i2, 1


def propose_between_routes(distance_matrix, cycle1, cycle2):
    for i1, i2 in itertools.product(range(len(cycle1)), range(len(cycle2))):
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
