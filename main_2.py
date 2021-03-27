import random
import time
from copy import deepcopy

import numpy as np

from lab1.connector import k_regret_connector
from lab1.distance_counter import count_dist, calculate_distance
from lab1.greedy_cycle import greedy_cycle_propose
from lab1.readFile import read_file
from lab1.visualize import animate, visualize, visualize2
from lab2.local_search import greedy, steepest, random_walk
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


if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '100.tsp')
    distance_matrix = count_dist(coordinates)

    path = [29, 17, 0, 22, 80, 94, 35, 60, 4, 57, 21, 58, 68, 15, 37, 69, 32, 10, 54, 89, 25, 79, 41, 53, 40, 11, 61,
            82, 1, 51, 97, 33, 46, 43, 67, 86, 99, 48, 62, 14, 44, 38, 90, 98, 3, 96, 18, 2, 87, 7, 73, 20, 16, 78, 76,
            12, 50, 85, 56, 47, 52, 59, 36, 95, 75, 83, 55, 26, 42, 84, 30, 45, 81, 31, 6, 88, 27, 23, 66, 39, 72, 93,
            91, 74, 64, 28, 34, 24, 8, 71, 5, 70, 63, 49, 65, 77, 92, 13, 19, 9]
    path1 = path[:50]
    path2 = path[50:]

    history = [[path1[:1], path2[:1]]]
    for i in range(2, 51):
        history.append([path1[:i], path2[:(i - 1)]])
        history.append([path1[:i], path2[:i]])

    paths = [path1, path2]
    execute_example(distance_matrix, steepest, propose_in_route, path1, path2, history)
    visualize2(history[-1], paths, coordinates)

# random
# 1. 187029.0,33412.0,153617.0,[[29, 17, 0, 22, 80, 94, 35, 60, 4, 57, 21, 58, 68, 15, 37, 69, 32, 10, 54, 89, 25, 79, 41, 53, 40, 11, 61, 82, 1, 51, 97, 33, 46, 43, 67, 86, 99, 48, 62, 14, 44, 38, 90, 98, 3, 96, 18, 2, 87, 7, 73, 20, 16, 78, 76, 12, 50, 85, 56, 47, 52, 59, 36, 95, 75, 83, 55, 26, 42, 84, 30, 45, 81, 31, 6, 88, 27, 23, 66, 39, 72, 93, 91, 74, 64, 28, 34, 24, 8, 71, 5, 70, 63, 49, 65, 77, 92, 13, 19, 9]]
# 2. 179870.0,37264.0,142606.0,[[20, 47, 45, 62, 19, 31, 87, 38, 25, 10, 43, 89, 39, 60, 2, 88, 17, 29, 82, 12, 4, 44, 55, 73, 50, 3, 27, 23, 32, 16, 34, 91, 33, 99, 52, 18, 53, 85, 63, 35, 51, 94, 93, 64, 58, 15, 61, 5, 97, 46, 95, 28, 77, 78, 90, 30, 54, 74, 42, 59, 14, 37, 41, 98, 24, 96, 40, 76, 67, 9, 11, 72, 7, 68, 92, 57, 80, 71, 21, 36, 83, 56, 48, 6, 79, 1, 22, 69, 86, 8, 84, 81, 13, 26, 65, 66, 70, 49, 75, 0]]
# 3. 186323.0,32722.0,153601.0,[[26, 14, 89, 0, 52, 7, 47, 62, 74, 11, 44, 32, 45, 76, 84, 35, 29, 31, 86, 5, 43, 10, 64, 71, 22, 8, 39, 21, 30, 20, 80, 51, 79, 9, 1, 4, 55, 54, 96, 24, 67, 53, 81, 73, 15, 42, 78, 56, 65, 2, 95, 60, 82, 61, 6, 46, 48, 77, 92, 49, 40, 87, 72, 12, 93, 58, 13, 99, 83, 25, 88, 66, 57, 70, 59, 19, 94, 75, 69, 18, 90, 41, 85, 50, 23, 27, 68, 91, 97, 63, 33, 28, 17, 98, 36, 38, 16, 37, 34, 3]]
# 4. 178230.0,41726.0,136504.0,[[30, 5, 58, 46, 88, 76, 86, 16, 19, 23, 8, 18, 39, 26, 0, 28, 42, 48, 53, 73, 45, 21, 77, 20, 4, 37, 40, 49, 55, 27, 78, 60, 68, 97, 65, 25, 56, 75, 11, 89, 67, 51, 22, 63, 17, 9, 32, 2, 83, 13, 74, 62, 52, 93, 69, 47, 80, 71, 24, 84, 38, 34, 44, 66, 98, 61, 43, 3, 57, 81, 31, 50, 91, 90, 15, 85, 72, 12, 79, 54, 10, 99, 7, 59, 92, 95, 87, 96, 6, 14, 36, 41, 82, 70, 29, 35, 1, 64, 33, 94]]
