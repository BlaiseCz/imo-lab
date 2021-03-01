from pprint import pprint
from readFile import read_file
from distance_counter import count_dist
from greedy_nearest_neighbour import greedy_nearest_neighbour
from greedy_cycle import greedy_cycle

if __name__ == '__main__':
    overview, coordinates = read_file('data/kroA100.tsp')
    # pprint(overview)
    # pprint(coordinates)

    distance_matrix = count_dist(coordinates)

    # for x in range(99):
    #     greedy_nearest_neighbour(distance_matrix, start_with=x)

    # for x in range(1):
    #     greedy_cycle(distance_matrix, start_with=x)
    greedy_cycle(distance_matrix, start_with=10)
    greedy_cycle(distance_matrix, start_with=0)
    greedy_cycle(distance_matrix, start_with=62)
    greedy_cycle(distance_matrix, start_with=46)


