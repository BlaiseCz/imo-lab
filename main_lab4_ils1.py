from hall_of_fame.read_file import read_file
from hall_of_fame.local_search import steepest
from hall_of_fame.start_result import k_regret
from hall_of_fame.perturbate import perturbateSmall_, perturbateBig_
from hall_of_fame.visualize import animate
from lab1.distance_counter import count_dist, calculate_distance
from time import time

def ils1(distance_matrix, time_allowed=5000):
    res = k_regret(distance_matrix)[-1]

    start = time()
    checkpoint = time()
    while True:
        res = steepest(distance_matrix, res[0], res[1])[-1]
        checkpoint = time()
        if checkpoint-start > time_allowed:
            break
        perturbateSmall_(res[0], res[1])
    return res

def ils2(distance_matrix, time_allowed=5000):
    res = k_regret(distance_matrix)[-1]

    start = time()
    checkpoint = time()
    while True:
        res = steepest(distance_matrix, res[0], res[1])[-1]
        checkpoint = time()
        if checkpoint-start > time_allowed:
            break
        perturbateBig_(res[0], res[1])
        res = k_regret(distance_matrix, start_with=res)[-1]
    return res

if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '200.tsp')
    distance_matrix = count_dist(coordinates)

    # # MSLS:
    # msls_results = []
    # for i in range(10):
    c1, c2 = ils1(distance_matrix)
    dist = calculate_distance(distance_matrix, c1) + \
           calculate_distance(distance_matrix,c2)
    print(dist)
    animate([c1, c2], coordinates, isCycle=[True, True])

