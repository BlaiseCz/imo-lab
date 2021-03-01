from pprint import pprint
from readFile import read_file
from distance_counter import count_dist
from greedy_nearest_neighbour import greedy_nearest_neighbour

if __name__ == '__main__':
    overview, coordinates = read_file('data/kroA100.tsp')
    # pprint(overview)
    # pprint(coordinates)

    distance_matrix = count_dist(coordinates)

    greedy_nearest_neighbour(distance_matrix)


