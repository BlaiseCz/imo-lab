from readFile import read_file
from distance_counter import count_dist
from greedy_nearest_neighbour import greedy_nearest_neighbour_propose
from greedy_cycle import calculate_dist_of_given_cycle, greedy_cycle_propose
from visualize import animate
from connector import turns_connector, k_regret_connector
import numpy as np


def calculate_path_dist(history_cycles, distance_matrix):
    distance1 = calculate_dist_of_given_cycle(history_cycles[0], distance_matrix)
    distance2 = calculate_dist_of_given_cycle(history_cycles[1], distance_matrix)
    return distance1, distance2




if __name__ == '__main__':
    data_set = 'kroA'
    overview, coordinates = read_file('data/' + data_set + '200.tsp')
    print(overview)
    distance_matrix = count_dist(coordinates)
    # resc, histc = greedy_cycle(distance_matrix, start_with=10)
    # resp, histp = greedy_nearest_neighbour(distance_matrix, start_with=10)


    results = []
    for x in range(100):
        history_gc, picked_nodes = turns_connector([greedy_cycle_propose,
                                      greedy_cycle_propose],
                                     distance_matrix)

        gc_dist_1, gc_dist_2 = calculate_path_dist(history_gc[-1], distance_matrix)
        results.append([gc_dist_1 + gc_dist_2, picked_nodes])
        # animate(history_gc, coordinates, cycle=[True, True])

    np_result = np.array(results, dtype=object)
    print(f'greedy_cycle minimum {np_result[:, 0].min(axis=0)} | maximum {np_result[:, 0].max(axis=0)} | mean {np_result[:, 0].mean(axis=0)}')
    np.savetxt('greedy_cycle-' + data_set + '.csv', np_result, delimiter=",", fmt="%s")

    results = []
    times = []

    for x in range(100):
        history_cycle, picked_nodes = k_regret_connector([greedy_cycle_propose,
                                            greedy_cycle_propose],
                                           distance_matrix, k=1)

        reg_gc_dist_1, reg_gc_dist_2 = calculate_path_dist(history_cycle[-1], distance_matrix)
        results.append([reg_gc_dist_1 + reg_gc_dist_2, picked_nodes])
        # animate(history_cycle, coordinates, cycle=[True, True])
        end = time.time()
        times.append(end - start)

    np_result = np.array(results, dtype=object)
    print(f'k-regret greedy_cycle minimum {np_result[:, 0].min(axis=0)} | maximum {np_result[:, 0].max(axis=0)} | mean {np_result[:, 0].mean(axis=0)}')
    np.savetxt('regret_greedy_cycle-' + data_set + '.csv', np_result, delimiter=",", fmt="%s")

    results = []
    for x in range(100):
        history_nn, picked_nodes = turns_connector([greedy_nearest_neighbour_propose,
                                      greedy_nearest_neighbour_propose],
                                     distance_matrix)

        nn_dist_1, nn_dist_2 = calculate_path_dist(history_nn[-1], distance_matrix)
        results.append([nn_dist_1 + nn_dist_2, picked_nodes])
        animate(history_nn, coordinates, cycle=[False, False])

    np_result = np.array(results, dtype=object)
    print(f'nearest neighbour minimum {np_result[:, 0].min(axis=0)} | maximum {np_result[:, 0].max(axis=0)} | mean {np_result[:, 0].mean(axis=0)}')
    np.savetxt('nn-' + data_set + '.csv', np_result, delimiter=",", fmt="%s")
