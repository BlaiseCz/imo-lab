def greedy_nearest_neighbour(distance_matrix):
    visited = []
    dist = 0
    current_id = 0
    all_visited = False

    while not all_visited:
        visited.append(current_id)

        node_distances = distance_matrix[current_id]
        min_dist = max(node_distances)
        for node_id, node_dist in enumerate(node_distances):
            if node_id not in visited:
                if node_dist < min_dist:
                    min_dist = node_id
                    current_id = node_id

        dist += min_dist

        if len(visited) == len(distance_matrix):
            all_visited = True

    print(dist)
    return dist
