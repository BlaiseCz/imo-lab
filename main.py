import random
from copy import deepcopy

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
    print(
        f'path1 = {dist_1} path2 = {dist_2}')
    path1, path2, history = algorithm(distance_matrix, path1, path2, propose_type, history)

    dist_1 = calculate_distance(distance_matrix, path1)
    dist_2 = calculate_distance(distance_matrix, path2)

    print(
        f'after local search\npath1 = {dist_1} path2 = {dist_2}  | with gain = {starting_dist - (dist_1 + dist_2)}')
    animate(history, coordinates, cycle=[True, True])


if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '100.tsp')
    distance_matrix = count_dist(coordinates)

    execute_example(distance_matrix, greedy, propose_in_route)
    execute_example(distance_matrix, greedy, propose_between_routes)

    execute_example(distance_matrix, steepest, propose_in_route)
    execute_example(distance_matrix, steepest, propose_between_routes)

    print(f'\n\nrandom cycles:\n')

    execute_example(distance_matrix, greedy, propose_in_route, start_type="random")
    execute_example(distance_matrix, greedy, propose_between_routes, start_type="random")

    execute_example(distance_matrix, steepest, propose_in_route, start_type="random")
    execute_example(distance_matrix, steepest, propose_between_routes, start_type="random")

    history, _ = k_regret_connector([greedy_cycle_propose,
                                     greedy_cycle_propose],
                                    distance_matrix, k=1)
    c1 = history[-1][0]
    c2 = history[-1][1]

    dist_1 = calculate_distance(distance_matrix, c1)
    dist_2 = calculate_distance(distance_matrix, c2)
    starting_dist = dist_1 + dist_2
    print(
        f'path1 = {dist_1} path2 = {dist_2}')
    best_cycle1, best_cycle2, history = random_walk(distance_matrix, c1, c2, propose_in_route, history, time_allowed=1)

    dist_1 = calculate_distance(distance_matrix, best_cycle1)
    dist_2 = calculate_distance(distance_matrix, best_cycle2)

    animate(history, coordinates, cycle=[True, True])
    print(
        f'after local search\npath1 = {dist_1} path2 = {dist_2}  | with gain = {starting_dist - (dist_1 + dist_2)}')
