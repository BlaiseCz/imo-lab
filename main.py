from pprint import pprint
from readFile import read_file
from distance_counter import count_dist, calculate_distance
from greedy_nearest_neighbour import greedy_nearest_neighbour, \
    greedy_nearest_neighbour_propose
from greedy_cycle import greedy_cycle, greedy_cycle_propose, calculate_dist_of_given_cycle
from visualize import visualize, animate
from connector import k_regret_connector, turns_connector
import numpy as np


def calculate_path_dist(history_cycles, distance_matrix):
    distance1 = calculate_dist_of_given_cycle(history_cycles[0], distance_matrix)
    distance2 = calculate_dist_of_given_cycle(history_cycles[1], distance_matrix)
    return distance1, distance2


if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '100.tsp')
    print(overview)
    distance_matrix = count_dist(coordinates)
    # resc, histc = greedy_cycle(distance_matrix, start_with=10)
    # resp, histp = greedy_nearest_neighbour(distance_matrix, start_with=10)


    results = []
    for x in range(100):
        history_gc = turns_connector([greedy_cycle_propose,
                                      greedy_cycle_propose],
                                     distance_matrix)

        gc_dist_1, gc_dist_2 = calculate_path_dist(history_gc[-1], distance_matrix)
        results.append([gc_dist_1 + gc_dist_2])
        # animate(history_gc, coordinates, cycle=[True, True])

    np_result = np.array(results)
    print(f'greedy_cycle minimum {np_result.min(axis=0)} | maximum {np_result.max(axis=0)} | mean {np_result.mean(axis=0)}')
    np.savetxt('greedy_cycle-' + data_set + '.csv', np_result, delimiter=",", fmt="%s")

    results = []
    for x in range(100):
        history_cycle = k_regret_connector([greedy_cycle_propose,
                                            greedy_cycle_propose],
                                           distance_matrix, k=1)

        reg_gc_dist_1, reg_gc_dist_2 = calculate_path_dist(history_cycle[-1], distance_matrix)
        results.append([reg_gc_dist_1 + reg_gc_dist_2])
        # animate(history_cycle, coordinates, cycle=[True, True])

    np_result = np.array(results)
    print(f'k-regret greedy_cycle minimum {np_result.min(axis=0)} | maximum {np_result.max(axis=0)} | mean {np_result.mean(axis=0)}')
    np.savetxt('regret_greedy_cycle-' + data_set + '.csv', np_result, delimiter=",", fmt="%s")

    results = []
    for x in range(100):
        history_nn = turns_connector([greedy_nearest_neighbour_propose,
                                      greedy_nearest_neighbour_propose],
                                     distance_matrix)

        nn_dist_1, nn_dist_2 = calculate_path_dist(history_nn[-1], distance_matrix)
        results.append([nn_dist_1 + nn_dist_2])
        # animate(history_nn, coordinates, cycle=[False, False])

    np_result = np.array(results)
    print(f'nearest neighbour minimum {np_result.min(axis=0)} | maximum {np_result.max(axis=0)} | mean {np_result.mean(axis=0)}')
    np.savetxt('nn-' + data_set + '.csv', np_result, delimiter=",", fmt="%s")
