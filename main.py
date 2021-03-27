import random
import time
from copy import deepcopy

import numpy as np

from lab1.connector import k_regret_connector
from lab1.distance_counter import count_dist, calculate_distance
from lab1.greedy_cycle import greedy_cycle_propose
from lab1.readFile import read_file
from lab1.visualize import animate
from lab2.local_search import greedy, steepest, random_walk
from lab2.propose import propose_in_route, propose_between_routes


# """
# 8 kombinacji:
#  steepest i greedy
#  losowy i kregret
#  zamiana zbiorów tworzące cykle (wymiana pomiedzy nimi), i ruch wewnątrztrasowe
#
# """

def execute_example(distance_matrix, algorithm, propose_type, start_type="k_regret"):
    if start_type == "k_regret":
        history, _ = k_regret_connector([greedy_cycle_propose,
                                         greedy_cycle_propose],
                                        distance_matrix, k=1)
        path1 = history[-1][0]
        path2 = history[-1][1]
    if start_type == "random":
        path = list(range(100))
        random.shuffle(path)
        path1 = path[:50]
        path2 = path[50:]
        history = [[path1[:1], path2[:1]]]
        for i in range(2, 51):
            history.append([path1[:i], path2[:(i - 1)]])
            history.append([path1[:i], path2[:i]])

    dist_1 = calculate_distance(distance_matrix, path1)
    dist_2 = calculate_distance(distance_matrix, path2)

    starting_dist = dist_1 + dist_2
    path1, path2, history = algorithm(distance_matrix, path1, path2, propose_type, history)

    dist_1 = calculate_distance(distance_matrix, path1)
    dist_2 = calculate_distance(distance_matrix, path2)

    return starting_dist, (dist_1 + dist_2)


if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '100.tsp')
    distance_matrix = count_dist(coordinates)

    algos = [[execute_example(distance_matrix, greedy, propose_in_route),
              "greedy_propose_in_route_k_regret"],
             [execute_example(distance_matrix, greedy, propose_between_routes),
              "greedy_propose_between_routes_k_regret"],
             [execute_example(distance_matrix, steepest, propose_in_route),
              "steepest_propose_in_route_k_regret"],
             [execute_example(distance_matrix, steepest, propose_between_routes),
              "steepest_propose_between_routes_k_regret"],
             [execute_example(distance_matrix, greedy, propose_in_route, start_type="random"),
              "greedy_propose_in_route_random"],
             [execute_example(distance_matrix, greedy, propose_between_routes, start_type="random"),
              "greedy_propose_between_routes_random"],
             [execute_example(distance_matrix, steepest, propose_in_route, start_type="random"),
              "steepest_propose_in_route_random"],
             [execute_example(distance_matrix, steepest, propose_between_routes, start_type="random"),
              "steepest_propose_between_routes_random"]
             ]

    results_to_save = []
    results = []
    times = []
    for algo in algos:
        for x in range(100):
            start = time.time()
            start_dist, end_dist = algo[0]
            results.append([start_dist, end_dist])
            times.append(time.time() - start)

        np_result = np.array(results, dtype=object)
        np_times = np.array(times, dtype=object)
        print(f'\n{algo[1]}')
        print(
            f'before | minimum {np_result[:, 0].min(axis=0)} | maximum {np_result[:, 0].max(axis=0)} | mean {np_result[:, 0].mean(axis=0)}')
        print(
            f'after | minimum  {np_result[:, 1].min(axis=0)} | maximum {np_result[:, 1].max(axis=0)} | mean {np_result[:, 1].mean(axis=0)}')
        print(f'job done in {np.sum(np_times)} | avg = {np.average(np_times)} | max = {np.max(np_times)}')

        results_to_save.append([algo[1],
                                np_result[:, 0].min(axis=0), np_result[:, 0].max(axis=0), np_result[:, 0].mean(axis=0),
                                np_result[:, 1].min(axis=0), np_result[:, 1].max(axis=0), np_result[:, 1].mean(axis=0)])

    np_results_to_save = np.array(results_to_save)
    np.savetxt(data_set + '.csv', np_results_to_save, delimiter=",", fmt="%s")

    # history, _ = k_regret_connector([greedy_cycle_propose,
    #                                  greedy_cycle_propose],
    #                                 distance_matrix, k=1)
    # c1 = history[-1][0]
    # c2 = history[-1][1]
    #
    # dist_1 = calculate_distance(distance_matrix, c1)
    # dist_2 = calculate_distance(distance_matrix, c2)
    # starting_dist = dist_1 + dist_2
    # print(
    #     f'path1 = {dist_1} path2 = {dist_2}')
    # best_cycle1, best_cycle2, history = random_walk(distance_matrix, c1, c2, propose_in_route, history, time_allowed=1)
    #
    # dist_1 = calculate_distance(distance_matrix, best_cycle1)
    # dist_2 = calculate_distance(distance_matrix, best_cycle2)
    #
    # animate(history, coordinates, cycle=[True, True])
    # print(
    #     f'after random walk\npath1 = {dist_1} path2 = {dist_2}  | with gain = {starting_dist - (dist_1 + dist_2)}')
