from pprint import pprint
from readFile import read_file
from distance_counter import count_dist
from greedy_nearest_neighbour import greedy_nearest_neighbour
from greedy_cycle import greedy_cycle
from visualize import visualize, animate

if __name__ == '__main__':
    overview, coordinates = read_file('data/kroA100.tsp')
    distance_matrix = count_dist(coordinates)
    resc, histc = greedy_cycle(distance_matrix, start_with=10)
    resp, histp = greedy_nearest_neighbour(distance_matrix, start_with=10)
    # greedy_cycle(distance_matrix, start_with=0)
    # greedy_cycle(distance_matrix, start_with=62)
    # greedy_cycle(distance_matrix, start_with=46)
    animate(histp, coordinates)
    visualize(resp, coordinates)
    animate(histc, coordinates)
    visualize(resc, coordinates)
