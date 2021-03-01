def greedy_cycle(distance_matrix, start_with):
    cycle = [start_with]

    current_node = distance_matrix[start_with]
    first_nearest_node_dist = sorted(current_node)[1]
    first_nearest_node_id = current_node.index(first_nearest_node_dist)

    cycle.append(first_nearest_node_id)

    while not len(cycle) == len(distance_matrix):
        nearest_node_id = find_node_closest_to_current_cycle(cycle, distance_matrix)
        cycle.append(nearest_node_id)

    print(cycle)
    return cycle


def find_node_closest_to_current_cycle(current_cycle, distance_matrix):
    min_node_id = len(distance_matrix)
    min_dist = {}

    for cycle_node_id in current_cycle:
        node = distance_matrix[cycle_node_id]
        min_node_dist = max(node)

        for node_id, node_dist in enumerate(node):
            if node_id not in current_cycle:
                if node_dist < min_node_dist:
                    min_node_dist = node_dist
                    min_node_id = node_id
        min_dist[min_node_id] = min_node_dist

    min_node_id = min(min_dist, key=min_dist.get)
    return min_node_id
