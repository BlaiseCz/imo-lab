from copy import deepcopy
from lab2.propose import propose_between_routes, propose_in_route

def steepest_local_search(distance_matrix, path1, path2=None):
    better_solution = True
    buff_path1 = deepcopy(path1)
    buff_path2 = deepcopy(path2)





    while better_solution:
        p = propose_in_route(distance_matrix, path1)
        lista_wszystkich_i1_i2_i_cost = list(p)

