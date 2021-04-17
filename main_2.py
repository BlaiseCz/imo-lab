import random
import time
from copy import deepcopy

import numpy as np

from lab1.connector import k_regret_connector
from lab1.distance_counter import count_dist, calculate_distance
from lab1.greedy_cycle import greedy_cycle_propose
from lab1.readFile import read_file
from lab1.visualize import animate, visualize, visualize2
from lab2.local_search import greedy, steepest_lab2, random_walk
from lab2.propose import propose_in_route, propose_between_routes


# """
# 8 kombinacji:
#  steepest i greedy
#  losowy i kregret
#  zamiana zbiorów tworzące cykle (wymiana pomiedzy nimi), i ruch wewnątrztrasowe
#
# """

def execute_example(distance_matrix, algorithm, propose_type, path1, path2, history):
    dist_1 = calculate_distance(distance_matrix, path1)
    dist_2 = calculate_distance(distance_matrix, path2)

    starting_dist = dist_1 + dist_2
    path1, path2, history = algorithm(distance_matrix, path1, path2, propose_type, history)

    dist_1 = calculate_distance(distance_matrix, path1)
    dist_2 = calculate_distance(distance_matrix, path2)

    return starting_dist, (dist_1 + dist_2)

def random_walk_test():
    path = [90, 18, 57, 44, 94, 51, 93, 86, 25, 5, 64, 38, 56, 15, 32, 0, 42, 81, 45, 26, 68, 63, 76, 58, 62, 19, 53,
            54, 16, 65, 1, 84, 73, 27, 23, 29, 3, 46, 55, 92, 12, 89, 48, 75, 82, 37, 41, 2, 71, 33, 78, 79, 70, 85, 61,
            6, 34, 22, 88, 9, 17, 69, 95, 77, 20, 21, 72, 97, 7, 40, 39, 67, 47, 49, 24, 35, 4, 98, 59, 52, 50, 60, 87,
            91, 10, 13, 31, 66, 99, 43, 11, 74, 14, 83, 80, 28, 8, 30, 36, 96]
    path1 = path[:50]
    path2 = path[50:]

    history = [[path1[:1], path2[:1]]]
    for i in range(2, 51):
        history.append([path1[:i], path2[:(i - 1)]])
        history.append([path1[:i], path2[:i]])

    animate(history[-1:], coordinates, cycle=[True, True])

    print(
        f'{calculate_distance(distance_matrix, history[-1][0]) + calculate_distance(distance_matrix, history[-1][1])}')

    best_cycle1, best_cycle2, history = random_walk(distance_matrix, history[-1][0], history[-1][1], propose_in_route,
                                                    history, time_allowed=8.8489)

    print(f'{calculate_distance(distance_matrix, best_cycle1) + calculate_distance(distance_matrix, best_cycle2)}')
    animate(history[-1:], coordinates, cycle=[True, True])

if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '100.tsp')
    distance_matrix = count_dist(coordinates)

    random_walk_test()
    # for random path
    # path = [90, 18, 57, 44, 94, 51, 93, 86, 25, 5, 64, 38, 56, 15, 32, 0, 42, 81, 45, 26, 68, 63, 76, 58, 62, 19, 53,
    #         54, 16, 65, 1, 84, 73, 27, 23, 29, 3, 46, 55, 92, 12, 89, 48, 75, 82, 37, 41, 2, 71, 33, 78, 79, 70, 85, 61,
    #         6, 34, 22, 88, 9, 17, 69, 95, 77, 20, 21, 72, 97, 7, 40, 39, 67, 47, 49, 24, 35, 4, 98, 59, 52, 50, 60, 87,
    #         91, 10, 13, 31, 66, 99, 43, 11, 74, 14, 83, 80, 28, 8, 30, 36, 96]
    # path1 = path[:50]
    # path2 = path[50:]

    # for k-regret
    history, picked_nodes = k_regret_connector([greedy_cycle_propose,
                                                greedy_cycle_propose],
                                               distance_matrix, start_with=[95, 80], k=1)

    animate(history[-1:], coordinates, cycle=[True, True])
    execute_example(distance_matrix, steepest_lab2, propose_between_routes, history[-1][0], history[-1][1], history)
    animate(history[-1:], coordinates, cycle=[True, True])

# random
# 1 29978.0,27211.0,2767.0,[[41, 24]]
# 2 30172.0,27557.0,2615.0,[[5, 98]]
# 3 31127.0,28429.0,2698.0,[[95, 80]]
# 4 31127.0,27948.0,3179.0,[[95, 80]]
# 5 189267.0,33868.0,155399.0,[[90, 18, 57, 44, 94, 51, 93, 86, 25, 5, 64, 38, 56, 15, 32, 0, 42, 81, 45, 26, 68, 63, 76, 58, 62, 19, 53, 54, 16, 65, 1, 84, 73, 27, 23, 29, 3, 46, 55, 92, 12, 89, 48, 75, 82, 37, 41, 2, 71, 33, 78, 79, 70, 85, 61, 6, 34, 22, 88, 9, 17, 69, 95, 77, 20, 21, 72, 97, 7, 40, 39, 67, 47, 49, 24, 35, 4, 98, 59, 52, 50, 60, 87, 91, 10, 13, 31, 66, 99, 43, 11, 74, 14, 83, 80, 28, 8, 30, 36, 96]]
# 6 189267.0,45190.0,144077.0,[[90, 18, 57, 44, 94, 51, 93, 86, 25, 5, 64, 38, 56, 15, 32, 0, 42, 81, 45, 26, 68, 63, 76, 58, 62, 19, 53, 54, 16, 65, 1, 84, 73, 27, 23, 29, 3, 46, 55, 92, 12, 89, 48, 75, 82, 37, 41, 2, 71, 33, 78, 79, 70, 85, 61, 6, 34, 22, 88, 9, 17, 69, 95, 77, 20, 21, 72, 97, 7, 40, 39, 67, 47, 49, 24, 35, 4, 98, 59, 52, 50, 60, 87, 91, 10, 13, 31, 66, 99, 43, 11, 74, 14, 83, 80, 28, 8, 30, 36, 96]]
# 7 189267.0,33616.0,155651.0,[[90, 18, 57, 44, 94, 51, 93, 86, 25, 5, 64, 38, 56, 15, 32, 0, 42, 81, 45, 26, 68, 63, 76, 58, 62, 19, 53, 54, 16, 65, 1, 84, 73, 27, 23, 29, 3, 46, 55, 92, 12, 89, 48, 75, 82, 37, 41, 2, 71, 33, 78, 79, 70, 85, 61, 6, 34, 22, 88, 9, 17, 69, 95, 77, 20, 21, 72, 97, 7, 40, 39, 67, 47, 49, 24, 35, 4, 98, 59, 52, 50, 60, 87, 91, 10, 13, 31, 66, 99, 43, 11, 74, 14, 83, 80, 28, 8, 30, 36, 96]]
# 8 189267.0,46140.0,143127.0,[[90, 18, 57, 44, 94, 51, 93, 86, 25, 5, 64, 38, 56, 15, 32, 0, 42, 81, 45, 26, 68, 63, 76, 58, 62, 19, 53, 54, 16, 65, 1, 84, 73, 27, 23, 29, 3, 46, 55, 92, 12, 89, 48, 75, 82, 37, 41, 2, 71, 33, 78, 79, 70, 85, 61, 6, 34, 22, 88, 9, 17, 69, 95, 77, 20, 21, 72, 97, 7, 40, 39, 67, 47, 49, 24, 35, 4, 98, 59, 52, 50, 60, 87, 91, 10, 13, 31, 66, 99, 43, 11, 74, 14, 83, 80, 28, 8, 30, 36, 96]]
