import random
import time

from lab1.connector import k_regret_connector
from lab1.distance_counter import count_dist
from lab1.greedy_cycle import greedy_cycle_propose
from lab1.readFile import read_file
from lab1.visualize import animate
from lab2.local_search import steepest_lab2
from lab3.effectiveness_improvement import lm_algorithm, lm_algorithm_ver2
from lab3.propose import propose_between_routes, propose_nodes_switch
import numpy as np


def calculate_path_dist(history_cycles, distance_matrix):
    distance1 = calculate_dist_of_given_cycle(history_cycles[0], distance_matrix)
    distance2 = calculate_dist_of_given_cycle(history_cycles[1], distance_matrix)
    return distance1, distance2

def calculate_dist_of_given_cycle(cycle, distance_matrix):
    dist = 0

    for x in range(len(cycle) - 1):
        dist += distance_matrix[cycle[x]][cycle[x + 1]]

    return dist

def generate_random_starting_paths(size=100):
    path = list(range(size))
    random.shuffle(path)
    path_first_part = path[:int(size/2)]
    path_second_part = path[int(size/2):]
    history = [[path_first_part[:1], path_second_part[:1]]]
    for i in range(2, int(size/2+1)):
        history.append([path_first_part[:i], path_second_part[:(i - 1)]])
        history.append([path_first_part[:i], path_second_part[:i]])

    return path_first_part, path_second_part, history


def test_best_from_lab1(distance_matrix):
    results = []
    times = []
    for x in range(100):
        start = time.time()

        history_cycle, picked_nodes = k_regret_connector([greedy_cycle_propose,
                                                          greedy_cycle_propose],
                                                         distance_matrix, k=1)

        reg_gc_dist_1, reg_gc_dist_2 = calculate_path_dist(history_cycle[-1], distance_matrix)
        results.append([reg_gc_dist_1 + reg_gc_dist_2, picked_nodes])
        end = time.time()
        times.append(end - start)
        # animate(history_cycle, coordinates, cycle=[True, True])
    np_result = np.array(results, dtype=object)
    np_times = np.array(times, dtype=object)
    print(
        f'k-regret greedy_cycle minimum {np_result[:, 0].min(axis=0)} | maximum {np_result[:, 0].max(axis=0)} | mean {np_result[:, 0].mean(axis=0)}')
    print(f'job done in {np.sum(np_times)} | avg = {np.average(np_times)} | max = {np.max(np_times)}')
    np.savetxt('lab3_best_from_lab1-' + data_set + '.csv', np_result, delimiter=",", fmt="%s")


if __name__ == '__main__':
    data_set = 'kroB'
    # data_set = 'kroA'
    overview, coordinates = read_file('data/' + data_set + '200.tsp')
    distance_matrix = count_dist(coordinates)

    # startujemy z losowych rozwiązań
    path1, path2, history = generate_random_starting_paths(size=200)

    # LM
    # history_cycle = lm_algorithm(distance_matrix,
    #                              path1, path2,
    #                              propose_nodes_switch,
    #                              history)
    # history_cycle = lm_algorithm_ver2(distance_matrix,
    #                              path1, path2,
    #                              propose_nodes_switch)
    #
    # animate(history_cycle, coordinates, cycle=[True, True])

    # Ruchy kandydackie

    # najlepszy z zadania 1
    test_best_from_lab1(distance_matrix)

    # lokalne przeszukiwanie w wersji stromej
    # cycle1, cycle2, history_ = steepest_lab2(distance_matrix,
    #                                         path1, path2,
    #                                         propose_between_routes,  # TODO: tutaj trzeba dla krawędzi wrzucic!!!
    #                                         history)
    # animate(history, coordinates, cycle=[True, True])
