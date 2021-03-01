def greedy_nearest_neighbour(distance_matrix):
    visited = [0]
    dist = 0
    current_id = 0
    all_visited = False

    copy_distance_matrix = distance_matrix[:]

    while not all_visited:
        visited.sort(reverse=True)
        node_distances = copy_distance_matrix[current_id]
        for visited_node in visited:
            node_distances.pop(visited_node)
        min_id = node_distances.index(min(node_distances))

        copy_distance_matrix.pop(current_id)
        current_id = min_id
        visited.append(min_id)
        dist += min(node_distances)

        if len(visited) == len(distance_matrix) - 2:
            all_visited = True

    print(dist)
    return dist
