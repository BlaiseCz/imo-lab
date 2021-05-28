from hall_of_fame.distance import calculate_distance, create_distance_matrix
from hall_of_fame.local_search import steepest
from hall_of_fame.read_file import read_file
from hall_of_fame.start_result import k_regret
from hall_of_fame.visualize import animate
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
    return (res[:cycle_len], res[cycle_len:])


def check_if_different_enough(solution, parents_with_res, min_edges_diff=4):
    """
    Liczymy ile jest krawędzi które nie występują w każdym rodzicu po kolei.
    """
    parents = [p[1] for p in parents_with_res]
    for parent in parents:
        new_edges_counter = 0
        for cycle in solution:
            for i, node in enumerate(cycle):
                if node in parent[0]:
                    idx = parent[0].index(node)
                    if     cycle[( i+1 )%len(cycle)] != \
                       parent[0][(idx+1)%len(parent[0])]:
                        new_edges_counter += 1
                else:
                    idx = parent[1].index(node)
                    if     cycle[( i+1 )%len(cycle)] != \
                       parent[1][(idx+1)%len(parent[1])]:
                        new_edges_counter += 1
        if new_edges_counter < min_edges_diff:
            return False

    return True


if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '100.tsp')
    distance_matrix = create_distance_matrix(coordinates)

    parents = generate_solutions(distance_matrix)
    parents = [(calculate_distance(distance_matrix, p), p) for p in parents]
    parents = sorted(parents)

    for _ in range(10):
        sol1, sol2 = pick_random_parents(parents)

        y = recombine(sol1, sol2)

        y = local_search(y)
        y_res = calculate_distance(distance_matrix, y)

        if y_res < parents[-1][0] and check_if_different_enough(y, parents):
            parents[-1] = (y_res, y)

