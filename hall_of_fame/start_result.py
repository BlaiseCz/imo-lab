from ._dependencies import k_regret_connector, greedy_cycle_propose
import random

def k_regret(distance_matrix, k=1, start_with=None):
    """
    Zwraca historię uzyskania rozwiązania początkowego za pomocą k-żalu.

    k-żal używa greedy cycle, a nie greedy nearest neighbour.
    """

    return k_regret_connector([greedy_cycle_propose, greedy_cycle_propose],
                              distance_matrix, k=k, start_with=start_with)[0]

def random_path(distance_matrix):
    """
    Zwraca historię uzyskania losowego rozwiązania początkowego (2 cykle).
    """
    size = len(distance_matrix)
    path = list(range(size))
    random.shuffle(path)
    path_first_part = path[:int(size/2)]
    path_second_part = path[int(size/2):]
    history = [[path_first_part[:1], path_second_part[:1]]]
    for i in range(2, int(size/2+1)):
        history.append([path_first_part[:i], path_second_part[:(i - 1)]])
        history.append([path_first_part[:i], path_second_part[:i]])

    return history

if __name__ == '__main__':
    from .read_file import read_file
    from .distance import create_distance_matrix
    from .visualize import animate
    _, coordinates = read_file('../data/kroA100.tsp')
    distance_matrix = create_distance_matrix(coordinates)
    animate(random_path(distance_matrix), coordinates, [True, True])

