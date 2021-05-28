from hall_of_fame.distance import calculate_distance
from hall_of_fame.local_search import steepest
from hall_of_fame.read_file import read_file
from hall_of_fame.start_result import random_path
from hall_of_fame.visualize import animate
from lab1.distance_counter import count_dist


def msls(distance_matrix, coordinates):
    random = random_path(distance_matrix)

    history = steepest(distance_matrix, random[-1][0], random[-1][1])
    return history[-1][0], history[-1][1]


if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '200.tsp')
    distance_matrix = count_dist(coordinates)

    # MSLS:
    msls_results = []
    for i in range(10):
        c1, c2 = msls(distance_matrix, coordinates)
        dist = calculate_distance(distance_matrix, c1, c2)
        msls_results.append([dist, c1, c2])

    print(min(msls_results))


