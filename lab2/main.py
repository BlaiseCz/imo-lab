import random
import time
from copy import deepcopy

import numpy as np

from lab1.connector import k_regret_connector
from lab1.distance_counter import count_dist, calculate_distance
from lab1.greedy_cycle import greedy_cycle_propose
from lab1.readFile import read_file
from lab2.local_search import greedy, steepest_lab2, random_walk
from lab2.propose import propose_in_route, propose_between_routes


# """
# 8 kombinacji:
#  steepest i greedy
#  losowy i kregret
#  zamiana zbiorów tworzące cykle (wymiana pomiedzy nimi), i ruch wewnątrztrasowe
#
# """

def execute_example_k_regret(distance_matrix, algorithm, propose_type, starting_history, picked_nodes):
    path1 = starting_history[-1][0]
    path2 = starting_history[-1][1]
    dist_1 = calculate_distance(distance_matrix, path1)
    dist_2 = calculate_distance(distance_matrix, path2)

    starting_dist = dist_1 + dist_2
    path1, path2, history = algorithm(distance_matrix, path1, path2, propose_type, starting_history)

    dist_1 = calculate_distance(distance_matrix, path1)
    dist_2 = calculate_distance(distance_matrix, path2)

    return starting_dist, (dist_1 + dist_2), picked_nodes

def execute_example_random(distance_matrix, algorithm, propose_type, starting_history, picked_nodes):
    path1 = starting_history[-1][0]
    path2 = starting_history[-1][1]
    dist_1 = calculate_distance(distance_matrix, path1)
    dist_2 = calculate_distance(distance_matrix, path2)

    starting_dist = dist_1 + dist_2
    path1, path2, history = algorithm(distance_matrix, path1, path2, propose_type, starting_history)

    dist_1 = calculate_distance(distance_matrix, path1)
    dist_2 = calculate_distance(distance_matrix, path2)

    return starting_dist, (dist_1 + dist_2), picked_nodes


if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '100.tsp')
    distance_matrix = count_dist(coordinates)

    # algos = [[distance_matrix, greedy, propose_in_route,
    #           "greedy_propose_in_route_k_regret"],
    #          [distance_matrix, greedy, propose_between_routes,
    #           "greedy_propose_between_routes_k_regret"],
    #          [distance_matrix, steepest, propose_in_route,
    #           "steepest_propose_in_route_k_regret"],
    #          [distance_matrix, steepest, propose_between_routes,
    #           "steepest_propose_between_routes_k_regret"]
    #          ]
    #
    # history_list = []
    # for _ in range(100):
    #     history, picked_nodes = k_regret_connector([greedy_cycle_propose,
    #                                      greedy_cycle_propose],
    #                                     distance_matrix, k=1)
    #     history_list.append([history, picked_nodes])
    #
    # results_to_save = []
    # for algo in algos:
    #     results = []
    #     times = []
    #     history_lits_copy = deepcopy(history_list)
    #     for history in history_lits_copy:
    #         start = time.time()
    #         start_dist, end_dist, picked_nodes = execute_example_k_regret(algo[0], algo[1], algo[2], history[0], history[1])
    #         results.append([start_dist, end_dist, (start_dist - end_dist), [picked_nodes]])
    #         end = time.time()
    #         times.append(end - start)
    #
    #     np_result = np.array(results, dtype=object)
    #     np_times = np.array(times, dtype=object)
    #     print(f'\n{algo[3]}')
    #     print(
    #         f'before | minimum {np_result[:, 0].min(axis=0)} | maximum {np_result[:, 0].max(axis=0)} | mean {np_result[:, 0].mean(axis=0)}')
    #     print(
    #         f'after | minimum  {np_result[:, 1].min(axis=0)} | maximum {np_result[:, 1].max(axis=0)} | mean {np_result[:, 1].mean(axis=0)}')
    #     print(
    #         f'gain | minimum  {np_result[:, 2].min(axis=0)} | maximum {np_result[:, 2].max(axis=0)} | mean {np_result[:, 2].mean(axis=0)}')
    #
    #     print(f'job done in {np.sum(np_times)} | avg = {np.average(np_times)} | max = {np.max(np_times)}')
    #
    #     np.savetxt(algo[3] + '.csv', np_result, delimiter=",", fmt="%s")
    #
    #     results_to_save.append([algo[1],
    #                             np_result[:, 0].min(axis=0), np_result[:, 0].max(axis=0), np_result[:, 0].mean(axis=0)]
    #                            )
    # np_results_to_save = np.array(results_to_save)
    # np.savetxt(data_set + '.csv', np_results_to_save, delimiter=",", fmt="%s")


    algos = [
             [distance_matrix, greedy, propose_in_route,
              "greedy_propose_in_route_random"],
             [distance_matrix, greedy, propose_between_routes,
              "greedy_propose_between_routes_random"],
             [distance_matrix, steepest_lab2, propose_in_route,
              "steepest_propose_in_route_random"],
             [distance_matrix, steepest_lab2, propose_between_routes,
              "steepest_propose_between_routes_random"]
             ]

    history_list = []
    for _ in range(100):
        path = list(range(100))
        random.shuffle(path)
        path1 = path[:50]
        path2 = path[50:]
        history = [[path1[:1], path2[:1]]]
        picked_nodes = path
        for i in range(2, 51):
            history.append([path1[:i], path2[:(i - 1)]])
            history.append([path1[:i], path2[:i]])

        history_list.append([history, picked_nodes])



    results_to_save = []
    for algo in algos:
        results = []
        times = []
        history_lits_copy = deepcopy(history_list)
        for history in history_lits_copy:
            start = time.time()
            start_dist, end_dist, picked_nodes = execute_example_k_regret(algo[0], algo[1], algo[2], history[0],
                                                                          history[1])
            results.append([start_dist, end_dist, (start_dist - end_dist), [picked_nodes]])
            end = time.time()
            times.append(end - start)

        np_result = np.array(results, dtype=object)
        np_times = np.array(times, dtype=object)
        print(f'\n{algo[3]}')
        print(
            f'before | minimum {np_result[:, 0].min(axis=0)} | maximum {np_result[:, 0].max(axis=0)} | mean {np_result[:, 0].mean(axis=0)}')
        print(
            f'after | minimum  {np_result[:, 1].min(axis=0)} | maximum {np_result[:, 1].max(axis=0)} | mean {np_result[:, 1].mean(axis=0)}')
        print(
            f'gain | minimum  {np_result[:, 2].min(axis=0)} | maximum {np_result[:, 2].max(axis=0)} | mean {np_result[:, 2].mean(axis=0)}')

        print(f'job done in {np.sum(np_times)} | avg = {np.average(np_times)} | max = {np.max(np_times)}')

        np.savetxt(algo[3] + '.csv', np_result, delimiter=",", fmt="%s")

        results_to_save.append([algo[1],
                                np_result[:, 0].min(axis=0), np_result[:, 0].max(axis=0), np_result[:, 0].mean(axis=0)]
                               )
    np_results_to_save = np.array(results_to_save)
    np.savetxt(data_set + '.csv', np_results_to_save, delimiter=",", fmt="%s")