from copy import deepcopy
from hall_of_fame.read_file import read_file
from hall_of_fame.distance import create_distance_matrix, calculate_distance
from hall_of_fame.start_result import random_path
from hall_of_fame.local_search import steepest, greedy

def generate_solutions(distance_matrix, num_of_sol=1000):
    solutions = []
    for i in range(num_of_sol):
        print(f'{i+1}/{num_of_sol}')
        solution = random_path(distance_matrix)[-1]
        solution = greedy(distance_matrix, solution[0], solution[1])[-1]
        solutions.append(solution)
    return solutions

def calculate_distances(distance_matrix, solutions):
    res = deepcopy(solutions)
    for i in range(len(res)):
        dist = calculate_distance(distance_matrix, res[i])
        res[i] = (dist, res[i])
    return res

def calculate_similarities(solutions, by_nodes=False):
    res = deepcopy(solutions)
    res = sorted(res)

    best = res[0][1]
    for i, sol in enumerate(res[1:]):
        res[i+1] = (*sol, calculate_similarity(best, sol[1], by_nodes))
    res[0] = [*res[0], 0]
    return res

def calculate_similarity(sol1, sol2, by_nodes):
    if by_nodes:
        res = 0
        res += min(len(set(sol1[0])&set(sol2[0])), len(set(sol1[0])&set(sol2[1])))
        res += min(len(set(sol1[1])&set(sol2[0])), len(set(sol1[1])&set(sol2[1])))
        return res
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
    overview, coordinates = read_file('data/' + data_set + '100.tsp')
    distance_matrix = create_distance_matrix(coordinates)

    # ustaw na ile rozwiązań to chcesz
    num_of_solutions = 1000

    solutions = generate_solutions(distance_matrix, num_of_solutions)
    solutions_with_dist = calculate_distances(distance_matrix, solutions)
    solutions = calculate_similarities(solutions_with_dist)
    solutions_by_nodes = calculate_similarities(solutions_with_dist, by_nodes=True)

    xs = [s[0] for s in solutions]
    ys = [s[2] for s in solutions]
    from statistics import mean, stdev
    from scipy.stats import pearsonr
    print(f'meanxs: {mean(xs)} , stdevxs: {stdev(xs)}')
    print(f'meanys: {mean(ys)} , stdevys: {stdev(ys)}')
    print(f'correlation: {pearsonr(xs, ys)[0]}')
    import matplotlib.pyplot as plt
    plt.scatter(xs[0], ys[0], label='best solution')
    plt.scatter(xs[1:], ys[1:], label='rest of solutions')
    plt.legend()
    plt.ylabel('Number of differences')
    plt.xlabel('Result')
    plt.title(f'Distribution of {num_of_solutions} solutions aquired by steepest search from random\n')
    plt.savefig('wypuklosc.png')
    plt.show()
    plt.close()

    print('*'*40)
    print('By nodes:')

xs = [s[0] for s in solutions_by_nodes]
ys = [s[2] for s in solutions_by_nodes]
print(f'meanxs: {mean(xs)} , stdevxs: {stdev(xs)}')
print(f'meanys: {mean(ys)} , stdevys: {stdev(ys)}')
print(f'correlation: {pearsonr(xs, ys)[0]}')
import matplotlib.pyplot as plt
plt.scatter(xs[0], ys[0], label='best solution')
plt.scatter(xs[1:], ys[1:], label='rest of solutions')
plt.legend()
plt.ylabel('Number of differences')
plt.xlabel('Result')
plt.title(f'Distribution of {num_of_solutions} solutions aquired by steepest search from random\n')
plt.savefig('wypuklosc_by_nodes_2.png')
    # plt.show()
