from pprint import pprint
from readFile import read_file
from distance_counter import count_dist
from greedy_nearest_neighbour import greedy_nearest_neighbour, \
greedy_nearest_neighbour_propose
from greedy_cycle import greedy_cycle, greedy_cycle_propose
from visualize import visualize, animate
from connector import k_regret_connector

if __name__ == '__main__':
    overview, coordinates = read_file('data/kroA100.tsp')
    print(overview)
    distance_matrix = count_dist(coordinates)
    # resc, histc = greedy_cycle(distance_matrix, start_with=10)
    # resp, histp = greedy_nearest_neighbour(distance_matrix, start_with=10)
    history_double_nn = k_regret_connector(greedy_nearest_neighbour_propose,
                                           greedy_cycle_propose,
                                           distance_matrix)
    # history_quadriple_nn = [(history_double_nn[i][0][::2],
    #                          history_double_nn[i][1][::2],
    #                          history_double_nn[i][0][1::2],
    #                          history_double_nn[i][1][1::2])\
    #                         for i in range(len(history_double_nn))]
    animate_two(history_double_nn, coordinates, cycle=[False, True])
