import random

from lab1.connector import k_regret_connector
from lab1.distance_counter import count_dist
from lab1.greedy_cycle import greedy_cycle_propose
from lab1.readFile import read_file
from lab1.visualize import animate
from lab2.local_search import steepest_lab2
from lab2.propose import propose_between_routes

if __name__ == '__main__':
    # data_set = 'kroB'
    data_set = 'kroA'
    overview, coordinates = read_file('data/' + data_set + '200.tsp')
    distance_matrix = count_dist(coordinates)

    #startujemy z losowych rozwiązań
    path = list(range(100))
    random.shuffle(path)
    path1 = path[:50]
    path2 = path[50:]

    #LM

    #Ruchy kandydackie

    #najlepszy z zadania 1
    history_cycle, _ = k_regret_connector([greedy_cycle_propose,
                                                      greedy_cycle_propose],
                                                     distance_matrix, k=1)

    animate(history_cycle, coordinates, cycle=[True, True])

    #lokalne przeszukiwanie w wersji stromej
    cycle1, cycle2, history = steepest_lab2(distance_matrix,
                                            history_cycle[-1][0], history_cycle[-1][-1],
                                            propose_between_routes, #TODO: tutaj trzeba dla krawędzi wrzucic!!!
                                            history_cycle)
    animate(history, coordinates, cycle=[True, True])
