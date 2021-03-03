from copy import deepcopy
import math

def greedy_nearest_neighbour(distance_matrix, start_with):
    visited = []
    history = []
    dist = 0
    current_id = start_with

    while not len(visited) == len(distance_matrix):
        visited.append(current_id)
        history.append(deepcopy(visited))

        node_distances = distance_matrix[current_id]
        min_dist = max(node_distances)

        for node_id, node_dist in enumerate(node_distances):
            if node_id not in visited:
                if node_dist < min_dist:
                    min_dist = node_dist
                    current_id = node_id

        dist += min_dist

    print(dist)
    return visited, history

def greedy_nearest_neighbour_propose(distance_matrix, visited, current_path):
    min_dist = math.inf
    min_id = -1
    current_id = current_path[-1]
    for node_id, node_dist in enumerate(distance_matrix[current_id]):
        if node_id not in visited:
            if node_dist < min_dist:
                min_dist = node_dist
                min_id = node_id
    current_path.append(min_id)
    return current_path, min_id
