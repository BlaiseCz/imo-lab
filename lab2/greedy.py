from copy import deepcopy
from random import sample

from lab1.distance_counter import calculate_distance
from lab2.propose import propose_between_routes, propose_in_route


def greedy_local_search(distance_matrix, path1, path2, swap_method):
    better_solution = True
    buff_path1 = deepcopy(path1)
    buff_path2 = deepcopy(path2)
    final_dist = float("inf")

    p1 = propose_in_route(distance_matrix, path1)
    p2 = propose_in_route(distance_matrix, path2)

    while better_solution:
        i1 = -1
        i2 = -1
        cost = -1

        # propose_in_route



        i1_1, i2_1, cost1 = next(p1)
        i1_2, i2_2, cost2 = next(p2)



        # if swap_method == "nodes":
        #     i1, i2, cost = propose_between_routes(distance_matrix, path1, path2)
        #
        #     if cost < 0:
        #         if path2 is None:
        #                 buff_path1[i1], buff_path1[i2] = buff_path1[i2], buff_path1[i1]

    return final_dist


def greedy_edges(path, distance_matrix, swap=6):
    better_solution = True
    better_solution_found = False
    best_path = deepcopy(path)
    buff_path = deepcopy(path)
    best_dist = calculate_distance(distance_matrix, path)

    history = [deepcopy(path)]

    while better_solution:
        starting_random_nodes = sample(list(range(len(distance_matrix))), 50)

        for node in starting_random_nodes:
            buff_path[node:swap + node] = buff_path[node:swap + node][::-1]
            updated_dist = calculate_distance(distance_matrix, buff_path)

            if updated_dist < best_dist:
                best_dist = updated_dist
                best_path = buff_path
                print(f'best dist = {best_dist}')
                better_solution_found = True
                history.append(deepcopy(best_path))
        if not better_solution_found:
            better_solution = False

    return best_path, best_dist, history


def greedy_nodes(path, distance_matrix):
    better_solution = True
    better_solution_found = False
    best_path = deepcopy(path)
    buff_path = deepcopy(path)
    best_dist = calculate_distance(distance_matrix, path)

    history = [deepcopy(path)]

    while better_solution:
        node_to_switch = sample(list(range(len(distance_matrix))), 2)

        buff_path[node_to_switch[0]], buff_path[node_to_switch[1]] = buff_path[node_to_switch[1]], buff_path[
            node_to_switch[0]]
        updated_dist = calculate_distance(distance_matrix, buff_path)

        if updated_dist < best_dist:
            best_dist = updated_dist
            best_path = buff_path
            print(f'best dist = {best_dist}')
            better_solution_found = True
            history.append(deepcopy(best_path))
        if not better_solution_found:
            better_solution = False

    return best_path, best_dist, history
