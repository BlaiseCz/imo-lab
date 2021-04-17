import random

from lab1.connector import k_regret_connector
from lab1.distance_counter import count_dist
from lab1.greedy_cycle import greedy_cycle_propose
from lab1.readFile import read_file
from lab1.visualize import animate
from lab2.local_search import steepest_lab2
from lab3.effectiveness_improvement import lm_algorithm
from lab3.propose import propose_between_routes


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


if __name__ == '__main__':
    # data_set = 'kroB'
    data_set = 'kroA'
    overview, coordinates = read_file('data/' + data_set + '200.tsp')
    distance_matrix = count_dist(coordinates)

    # startujemy z losowych rozwiązań
    path1, path2, history = generate_random_starting_paths(size=200)

    # LM
    history_cycle = lm_algorithm(distance_matrix,
                                 path1, path2,
                                 propose_between_routes,
                                 history)

    animate(history_cycle, coordinates, cycle=[True, True])

    # Ruchy kandydackie

    # najlepszy z zadania 1
    history_cycle, _ = k_regret_connector([greedy_cycle_propose,
                                           greedy_cycle_propose],
                                          distance_matrix, k=1)

    animate(history_cycle, coordinates, cycle=[True, True])

    # lokalne przeszukiwanie w wersji stromej
    cycle1, cycle2, history = steepest_lab2(distance_matrix,
                                            path1, path2,
                                            propose_between_routes,  # TODO: tutaj trzeba dla krawędzi wrzucic!!!
                                            history_cycle)
    animate(history, coordinates, cycle=[True, True])
