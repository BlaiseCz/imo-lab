from lab1.connector import k_regret_connector
from lab1.distance_counter import count_dist
from lab1.greedy_cycle import greedy_cycle_propose
from lab1.readFile import read_file
from lab1.visualize import animate
from lab2.greedy import greedy_edges
from lab2.random_path_generator import generate_random_path

if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('../data/' + data_set + '100.tsp')
    distance_matrix = count_dist(coordinates)
    random_path1, random_path2 = generate_random_path(int(overview['DIMENSION']))

    history, _ = k_regret_connector([greedy_cycle_propose],
                                    distance_matrix, k=1)
    kk_path1 = history[-1][0]
    print(kk_path1)
    path, dist, hist = greedy_edges(kk_path1, distance_matrix)
    animate(hist, coordinates, cycle=[True])

