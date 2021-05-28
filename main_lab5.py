from hall_of_fame.distance import calculate_distance
from hall_of_fame.local_search import steepest
from hall_of_fame.read_file import read_file
from hall_of_fame.start_result import k_regret
from hall_of_fame.visualize import animate
from lab1.distance_counter import count_dist
import random


def generate_solutions(distance_matrix, iter=50):
    solutions = []

    for _ in range(iter):
        solutions.append(k_regret(distance_matrix)[-1])

    return solutions


def pick_random_parents(parents):
    p1, p2 = random.choices(parents, k=2)
    return p1, p2


def recombine(sol1, sol2):
    pass


if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '100.tsp')
    distance_matrix = count_dist(coordinates)

    parents = generate_solutions(distance_matrix)

    counter = 0

    while counter < 10:
        sol1, sol2 = pick_random_parents(parents)

        y = recombine(sol1, sol2)

        y = local_search(y)

        counter += 1
