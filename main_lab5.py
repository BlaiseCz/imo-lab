from hall_of_fame.distance import calculate_distance, create_distance_matrix
from hall_of_fame.local_search import steepest
from hall_of_fame.read_file import read_file
from hall_of_fame.start_result import k_regret
from hall_of_fame.visualize import animate
import random


def generate_solutions(distance_matrix, iter=20):
    solutions = []

    for _ in range(iter):
        solutions.append(k_regret(distance_matrix)[-1])

    return solutions


def pick_random_parents(parents):
    p1, p2 = random.choices(parents, k=2)
    return p1, p2


def recombine(sol1, sol2):
    """
    wersja ze strony 33 (była najprostsza)
    """
    res = []
    cycle_len = len(sol1[0])
    s = [sol1[0] + sol1[1], sol2[0] + sol2[1]]
    for i in range(len(s[0])):
        cycle_chosen = random.randint(0, 1)
        node_chosen = s[cycle_chosen][0]
        res.append(node_chosen)
        s[0].remove(node_chosen)
        s[1].remove(node_chosen)
    ret = (res[:cycle_len], res[cycle_len:])

    if not ret:
        print("here")
    return ret


def check_if_different_enough(solution, parents_with_res, min_edges_diff=4):
    """
    Liczymy ile jest krawędzi które nie występują w każdym rodzicu po kolei.
    """
    parents = [p[1] for p in parents_with_res]
    for parent in parents:
        new_edges_counter = 0
        for cycle in solution:
            for i, node in enumerate(cycle):
                try:
                    if node in parent[0]:
                        idx = parent[0].index(node)
                        if cycle[(i + 1) % len(cycle)] != parent[0][(idx + 1) % len(parent[0])]:
                            new_edges_counter += 1
                    else:
                        idx = parent[1].index(node)
                        if cycle[(i + 1) % len(cycle)] != parent[1][(idx + 1) % len(parent[1])]:
                            new_edges_counter += 1
                except Exception:
                    print(node)
                    print(parent)

        if new_edges_counter < min_edges_diff:
            return False

    return True


import sys

if __name__ == '__main__':

    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '200.tsp')
    distance_matrix = create_distance_matrix(coordinates)
    iter = 20

    try:
        if sys.argv[1] is not None:
            iter = int(sys.argv[1])
        print('parameter passed ', iter)
    except IndexError:
        print('no parameters passed...')

    print('num of iterations ', iter)
    parents = generate_solutions(distance_matrix, iter=iter)
    parents = [(calculate_distance(distance_matrix, p), p) for p in parents]
    parents = sorted(parents)

    for i in range(10):
        sol1, sol2 = pick_random_parents(parents)

        y = recombine(sol1[1], sol2[1])
        y = steepest(distance_matrix, y[0], y[1])
        y_res = calculate_distance(distance_matrix, y[-1])

        if y_res < parents[-1][0] and check_if_different_enough(y[-1], parents):
            parents[-1] = (y_res, y[-1])

        parents = sorted(parents)
        print(i)

    print(min(parents))
