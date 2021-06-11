from copy import deepcopy
from hall_of_fame.read_file import read_file
from hall_of_fame.distance import create_distance_matrix, calculate_distance
from hall_of_fame.start_result import random_path
from hall_of_fame.local_search import steepest

def generate_solutions(distance_matrix, num_of_sol=1000):
    solutions = []
    for i in range(num_of_sol):
        print(f'{i+1}/{num_of_sol}')
        solution = random_path(distance_matrix)[-1]
        print('got random')
        solution = steepest(distance_matrix, solution[0], solution[1])[-1]
        print('got steepest')
        solutions.append(solution)
    return solutions

def calculate_distances(distance_matrix, solutions):
    res = deepcopy(solutions)
    for i in range(len(distance_matrix)):
        dist = calculate_distance(distance_matrix, res[i])
        res[i] = (dist, res[i])
    return res

def calculate_similarities(solutions):
    res = deepcopy(solutions)
    res = sorted(res)

    best = res[0]
    for i, sol in enumerate(res[1:]):
        res[i] = (*sol, calculate_similarity(best, sol[1]))
    return res

def calculate_similarity(sol1, sol2):
    same_edges_counter = 0
    for cycle in sol1:
        for i, node in enumerate(cycle):
            if node in sol2[0]:
                idx = sol2[0].index(node)
                if cycle[(i + 1) % len(cycle)] == sol2[0][(idx + 1) %
                                                          len(sol2[0])]:
                    same_edges_counter += 1
            else:
                idx = sol2[1].index(node)
                if cycle[(i + 1) % len(cycle)] == sol2[1][(idx + 1) %
                                                          len(sol2[1])]:
                    same_edges_counter += 1
    return same_edges_counter


if __name__ == '__main__':

    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '200.tsp')
    distance_matrix = create_distance_matrix(coordinates)

    solutions = generate_solutions(distance_matrix, 10)
    solutions = calculate_distances(distance_matrix, solutions)
    solutions = calculate_similarities(solutions)

    xs = [s[0] for s in solutions]
    ys = [s[2] for s in solutions]
    import matplotlib.pyplot as plt
    plt.scatter(xs, ys)

