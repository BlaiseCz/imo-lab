from copy import deepcopy

from lab1.connector import k_regret_connector
from lab1.distance_counter import count_dist, calculate_distance
from lab1.greedy_cycle import greedy_cycle_propose
from lab1.readFile import read_file
from lab1.visualize import animate
from lab2.local_search import greedy, steepest
from lab2.propose import propose_in_route, propose_between_routes
from lab2.random_path_generator import generate_random_path


# """
# 8 kombinacji:
#  steepest i greedy
#  losowy i kregret
#  zamiana zbiorów tworzące cykle (wymiana pomiedzy nimi), i ruch wewnątrztrasowe
#
# """

def execute_example(distance_matrix, algorithm, propose_type):
    history, _ = k_regret_connector([greedy_cycle_propose,
                                     greedy_cycle_propose],
                                    distance_matrix, k=1)
    kk_path1 = history[-1][0]
    kk_path2 = history[-1][1]

    dist_1 = calculate_distance(distance_matrix, kk_path1)
    dist_2 = calculate_distance(distance_matrix, kk_path2)
    starting_dist = dist_1 + dist_2
    print(
        f'path1 = {dist_1} path2 = {dist_2}')
    kk_path1, kk_path2, history = algorithm(distance_matrix, kk_path1, kk_path2, propose_type, history)

    dist_1 = calculate_distance(distance_matrix, kk_path1)
    dist_2 = calculate_distance(distance_matrix, kk_path2)

    print(
        f'after local search\npath1 = {dist_1} path2 = {dist_2}  | with gain = {starting_dist - (dist_1 + dist_2)}')
    animate(history, coordinates, cycle=[True, True])


if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '100.tsp')
    distance_matrix = count_dist(coordinates)
    random_path1, random_path2 = generate_random_path(int(overview['DIMENSION']))

    execute_example(distance_matrix, greedy, propose_in_route)
    execute_example(distance_matrix, greedy, propose_between_routes)

    execute_example(distance_matrix, steepest, propose_in_route)
    execute_example(distance_matrix, steepest, propose_between_routes)
