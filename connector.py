from copy import deepcopy
def k_regret_connector(algo_1, algo_2, distance_matrix, k=1):
    visited = [1, 10]

    # TODO randomize start node
    cycle_1 = [1]
    cycle_2 = [10]

    history = []

    if k > 1:
        raise NotImplementedError
    #     for i in range(len(distance_matrix)):
    #         # TODO: zapisywać żal
    #         for j in range(k):
    #             cycle_1_new, visited_node_1 = algo_1(distance_matrix, visited, cycle_1)
    #             cycle_2_new, visited_node_2 = algo_2(distance_matrix, visited, cycle_2)
    else:
        i = 0
        while len(visited) != len(distance_matrix):
            if i%2 == 0:
                cycle_1, visited_node = algo_1(distance_matrix, visited, cycle_1)
            else:
                cycle_2, visited_node = algo_2(distance_matrix, visited, cycle_2)
            history.append(deepcopy((cycle_1, cycle_2)))
            visited.append(visited_node)
            i += 1
        return history
