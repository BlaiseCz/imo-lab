from lab1.connector import k_regret_connector
from lab1.distance_counter import count_dist
from lab1.greedy_cycle import greedy_cycle_propose
from lab1.readFile import read_file
from lab1.visualize import animate
from lab2.greedy import greedy_edges, greedy_local_search
from lab2.propose import propose_in_route, propose_between_routes
from lab2.random_path_generator import generate_random_path


# """
# 8 kombinacji:
#  steepest i greedy
#  losowy i kregret
#  zamiana zbiorów tworzące cykle (wymiana pomiedzy nimi), i ruch wewnątrztrasowe
# """
if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '100.tsp')
    distance_matrix = count_dist(coordinates)
    random_path1, random_path2 = generate_random_path(int(overview['DIMENSION']))

    history, _ = k_regret_connector([greedy_cycle_propose,
                                     greedy_cycle_propose],
                                    distance_matrix, k=1)
    kk_path1 = history[-1][0]
    kk_path2 = history[-1][1]
    print(kk_path1)

    # --------------------- tutorial użycia ------------------------------
    # NOTE: bez różnicy której funkcji propose używasz

    # GREEDY:
    for gain, i1, i2, num in propose_in_route(distance_matrix,kk_path1,kk_path2):
        # i1 należy do pierwszego cycle, i2 do drugiego
        if num == 2:
            pass
        # oba i należą do pierwszego
        elif num == 0:
            pass
        # oba i należą do drugiego
        elif num == 1:
            pass


    # STEEPEST:
    proposals = list(propose_between_routes(distance_matrix, kk_path1, kk_path2))
    # najlepsza opcja
    num, i1, i2, gain = max(proposals)

    # --------------------------------------------------------------------
    greedy_local_search(distance_matrix, kk_path1, kk_path2, propose_in_route)

    greedy_local_search(distance_matrix, kk_path1, kk_path2, propose_between_routes)

    path, dist, hist = greedy_edges(kk_path1, distance_matrix)

    animate(hist, coordinates, cycle=[True])

