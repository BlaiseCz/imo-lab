from hall_of_fame.read_file import read_file
from lab1.distance_counter import count_dist, calculate_distance


def ils1(distance_matrix, coordinates):
    pass


if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '200.tsp')
    distance_matrix = count_dist(coordinates)

    # MSLS:
    msls_results = []
    for i in range(10):
        c1, c2 = ils1(distance_matrix, coordinates)
        dist = calculate_distance(distance_matrix, c1, c2)
        msls_results.append([dist, c1, c2])

    print(min(msls_results))
